from requests import post, get
from lxml import html

login_url = 'https://trialstore999.myshopify.com/admin/auth/login'
login_data = {
	'commit': 'Log in',
	'login': 'aznapn@hotmail.ca',
	'password': 'shopify',
	'utf8': '\\u2713'
}

login_headers = {
	'Accept': (
		'text/html,application/xhtml+xml,application/xml;q=0.9,'
		'image/webp,*/*;q=0.8'
		),
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
}

login_resp = post(login_url, headers=login_headers, data=login_data)



dis_url = 'https://trialstore999.myshopify.com/admin/discounts/new'

dis_headers = login_headers
dis_headers.pop('Content-Type', None)
dis_headers['Cookie'] = login_resp.request.headers['Cookie']

dis_resp = get(dis_url, headers=dis_headers)

tree = html.fromstring(dis_resp.content)

auth_token = tree.xpath("//form[@id='new_discount']//input[@name='authenticity_token']/@value")[0]

#print login_resp.request.headers['Cookie']
#_secure_admin_session_id=9dc9c648791fe69fc3748e60c816cd36; storefront_digest=47771bea39c6b4e65a0ef42f8f541db943ee2b041eadd1a44fedb6aa5c0a1c6b; request_method=POST; _ab=1





discount_url = 'https://trialstore999.myshopify.com/admin/discounts'

discount_params = {
	'utf8':'\\u2713',
	'authenticity_token': auth_token,
	'discount[code]':'python3',
	'discount[discount_type]':'fixed_amount',
	'discount[value]':5,
	'discount[applies_to_resource]':'minimum_order_amount',
	'discount[minimum_order_amount]':0.00,
	'usage_limit_type':'no_limit',
	'discount[usage_limit]': '',
	'discount[applies_once_per_customer]':0,
	'discount[applies_once_per_customer]':1,
	'discount[starts_at]':'2016-05-03',
	'discount_never_expires': '',
}

discount_headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Cookie':'_secure_admin_session_id=4489041a54d6feaa3e9b04a935ba0e5e; __ssid=887ffbbf-f26e-4a8e-90a2-36f81c4bc75a; ajs_anonymous_id=%220ba449dc-08cf-4a59-b5e0-0443f248ff3e%22; _ab=1; storefront_digest=47771bea39c6b4e65a0ef42f8f541db943ee2b041eadd1a44fedb6aa5c0a1c6b; use_unsupported_browsers=true; __utmt=1; _gat=1; ajs_user_id=null; ajs_group_id=null; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _ga=GA1.2.1008795743.1462321068; __utma=1.1008795743.1462321068.1462321068.1462321068.1; __utmb=1.9.10.1462321068; __utmc=1; __utmz=1.1462321068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
}

del discount_headers['Cookie']

discount_headers['Cookie'] = login_resp.request.headers['Cookie']

discount_resp = post(discount_url, headers=discount_headers, data=discount_params)

print discount_resp.status_code

print discount_resp.headers
print discount_resp.request.headers

print discount_resp.content
