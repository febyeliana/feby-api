from flask import Flask, request, jsonify
from scrap import scrape_item_from_tokped


app = Flask(__name__)


@app.route('/search')
def search_product():
	data = request.args

	if 'keyword' not in data:
		return jsonify({'error': 'Query not found'}), 400

	item_name = data['keyword']
	return jsonify(scrape_item_from_tokped(item_name))


if __name__ == "__main__":
	app.run()