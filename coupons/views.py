from django.shortcuts import render
from django.http import HttpResponse

from requests import get, post
from lxml import html
from datetime import date


def display_main(request):
	return render(request, 'index.html')

def submit(request):
	if request.method != 'POST':
		return HttpResponse('Incorrect request type')
	elif (
		'StoreName' not in request.POST or 'InputEmail' not in request.POST \
		or 'InputPassword' not in request.POST or 'InputCoupon' not in \
		request.POST or 'CouponType' not in request.POST or 'InputValue' \
		not in request.POST or 'InputOrder' not in request.POST
	):
		return HttpResponse('Incorrect parameters')

	try:
		store_name = request.POST['StoreName'].lower()
		email = request.POST['InputEmail']
		password = request.POST['InputPassword']
		coupon_name = request.POST['InputCoupon']

		coupon_type = request.POST['CouponType']

		if coupon_type == 'Fixed Dollar':
			coupon_type = 'fixed_amount'
		else:
			coupon_type = 'percentage'

		coupon_value = float(request.POST['InputValue'])
		min_order = float(request.POST['InputOrder'])

	except ValueError:
		return HttpResponse('Require valid numbers for values')

	#Perform First Request
	login_url = 'https://{0}.myshopify.com/admin/auth/login'.format(store_name)
	login_data = {
		'commit': 'Log in',
		'login': email,
		'password': password,
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

	#Perform Second Request
	dis_url = (
		'https://{0}.myshopify.com/admin/discounts/new'.format(store_name)
	)

	dis_headers = login_headers
	dis_headers.pop('Content-Type', None)

	try:
		dis_headers['Cookie'] = login_resp.request.headers['Cookie']
	except KeyError:
		return HttpResponse('Authentication process at Shopify failed')

	dis_resp = get(dis_url, headers=dis_headers)

	tree = html.fromstring(dis_resp.content)

	auth_token = tree.xpath(
		"//form[@id='new_discount']//input[@name='authenticity_token']/@value"
	)[0]

	#Perform Final Request
	discount_url = (
		'https://{0}.myshopify.com/admin/discounts'.format(store_name)
	)

	discount_params = {
		'utf8':'\\u2713',
		'authenticity_token': auth_token,
		'discount[code]': coupon_name,
		'discount[discount_type]': coupon_type,
		'discount[value]': coupon_value,
		'discount[applies_to_resource]':'minimum_order_amount',
		'discount[minimum_order_amount]': min_order,
		'usage_limit_type':'no_limit',
		'discount[usage_limit]': '',
		'discount[applies_once_per_customer]':0,
		'discount[starts_at]': date.today().strftime('%Y-%m-%d'),
		'discount_never_expires': '',
	}

	discount_headers = login_headers

	discount_headers['Cookie'] = login_resp.request.headers['Cookie']

	discount_resp = post(
		discount_url,
		headers=discount_headers,
		data=discount_params
	)

	return_string = (
		'Discount code {0} created. Please check your shopify admin page '
		'to confirm discount code is present.'.format(coupon_name)
	)

	return HttpResponse(return_string)
