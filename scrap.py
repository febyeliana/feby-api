import requests
import json

TOKPED_URL = 'https://ta.tokopedia.com/v1.1/display?q={}&page=1&ep=product&item=100&src=search&device=desktop&user_id=0&minimum_item=100&no_autofill_range=1-1'


def format_product(item):
	result = {}
	product = item['product']
	result['name'] = product['name']
	result['image'] = product['image']['xs_url']
	result['url'] = product['uri']
	result['price'] = product['price']
	result['formatted_price'] = product['price_format']
	result['rating'] = product['product_rating']

	return result


def scrape_item_from_tokped(item_name):
	x = item_name.replace(' ', '+')
	search_url = TOKPED_URL.format(x)
	success = False

	while not success:
		try:
			r = requests.get(search_url)
		except:
			continue

		success = True

	data = json.loads(r.text)
	products = data['data']
	result = []
	for item in products:
		result.append(format_product(item))

	min_autofill = data['guide']['autofill']['start']
	max_autofill = data['guide']['autofill']['end']
	filtered_result = []
	
	for i in range(len(result)):
		if i <= max_autofill and i >= min_autofill:
			continue
		filtered_result.append(result[i])

	return filtered_result
