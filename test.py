headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Length':513,
	'Content-Type':'application/x-www-form-urlencoded',
	'Cookie':'_secure_admin_session_id=4489041a54d6feaa3e9b04a935ba0e5e; __ssid=887ffbbf-f26e-4a8e-90a2-36f81c4bc75a; ajs_anonymous_id=%220ba449dc-08cf-4a59-b5e0-0443f248ff3e%22; _ab=1; storefront_digest=47771bea39c6b4e65a0ef42f8f541db943ee2b041eadd1a44fedb6aa5c0a1c6b; use_unsupported_browsers=true; __utmt=1; _gat=1; ajs_user_id=null; ajs_group_id=null; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _ga=GA1.2.1008795743.1462321068; __utma=1.1008795743.1462321068.1462321068.1462321068.1; __utmb=1.9.10.1462321068; __utmc=1; __utmz=1.1462321068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	'Host':'trialstore999.myshopify.com',
	'Origin':'https://trialstore999.myshopify.com',
	'Referer':'https://trialstore999.myshopify.com/admin/discounts/new',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
}

# TO Create the coupon
params = {
	'utf8':'✓',
	'authenticity_token':'Phi0C/HCnPIRQWrsSaNfgN05SaEu83kB1BK1TVe3+DMMuTggoTBDSLmEJxSqBS6pkEOJ7rEE8ZhQaPTqnLThDg==',
	'discount[code]':'discount_from_python2',
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

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Cookie':'_secure_admin_session_id=4489041a54d6feaa3e9b04a935ba0e5e; __ssid=887ffbbf-f26e-4a8e-90a2-36f81c4bc75a; ajs_anonymous_id=%220ba449dc-08cf-4a59-b5e0-0443f248ff3e%22; _ab=1; storefront_digest=47771bea39c6b4e65a0ef42f8f541db943ee2b041eadd1a44fedb6aa5c0a1c6b; use_unsupported_browsers=true; __utmt=1; _gat=1; ajs_user_id=null; ajs_group_id=null; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _ga=GA1.2.1008795743.1462321068; __utma=1.1008795743.1462321068.1462321068.1462321068.1; __utmb=1.9.10.1462321068; __utmc=1; __utmz=1.1462321068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'
}

'''
Requred parameters:
store name
name of coupon
username
password
fixed/percent
value of discount
apply to orders over
'''
'''----------------------------------------------'''

#To Create

headers2 = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
}

#Cookie:login_style=login; _secure_admin_session_id=f2a4c1bd4134394c9ce97e92fe5b1e2f; __ssid=887ffbbf-f26e-4a8e-90a2-36f81c4bc75a; ajs_anonymous_id=%220ba449dc-08cf-4a59-b5e0-0443f248ff3e%22; use_unsupported_browsers=true; __utmt=1; __utma=1.1008795743.1462321068.1462321068.1462321068.1; __utmb=1.16.10.1462321068; __utmc=1; __utmz=1.1462321068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1008795743.1462321068; _gat=1; ajs_user_id=null; ajs_group_id=null; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_s=F4D23831-BA7C-4D12-9F6F; _shopify_y=98A2B7C6-B71A-4FAC-08E8; _shopify_y=98A2B7C6-B71A-4FAC-08E8

params2 = {
	'utf8':'✓',
	'login':'aznapn@hotmail.ca',
	'password':'shopify',
	'commit':'Log in',
}

#	authenticity_token:N5W1TDCQ0MRfj6CqbIdxM9AOOtENbdYkFgFmv6vNlYbtWWsUCa7fj/YiHAGpIisAoOL1AE9JSQH1JipEpXOGjg==
#redirect:

'Cookie':
_secure_admin_session_id=4489041a54d6feaa3e9b04a935ba0e5e; 
__ssid=887ffbbf-f26e-4a8e-90a2-36f81c4bc75a; 
ajs_anonymous_id=%220ba449dc-08cf-4a59-b5e0-0443f248ff3e%22; 
_ab=1; 
storefront_digest=47771bea39c6b4e65a0ef42f8f541db943ee2b041eadd1a44fedb6aa5c0a1c6b; 
use_unsupported_browsers=true; 
__utmt=1; _gat=1; 
ajs_user_id=null; 
ajs_group_id=null; 
_shopify_s=F4D23831-BA7C-4D12-9F6F; 
_shopify_s=F4D23831-BA7C-4D12-9F6F; 
_shopify_y=98A2B7C6-B71A-4FAC-08E8; 
_shopify_y=98A2B7C6-B71A-4FAC-08E8; 
_ga=GA1.2.1008795743.1462321068; 
__utma=1.1008795743.1462321068.1462321068.1462321068.1; 
__utmb=1.9.10.1462321068; __utmc=1; 
__utmz=1.1462321068.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none),


#xpath to get authenticity token:
# //form[@id='new_discount']//input[@name='authenticity_token']/@value
