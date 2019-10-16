from http.server import HTTPServer, BaseHTTPRequestHandler
from scrap import scrape_item_from_tokped
import json
import re

class SearchHandler(BaseHTTPRequestHandler):
    def respond_json(self, data, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def get_keyword(self):
        keyword = re.findall(r"keyword=([^\&]+)", self.path)
        return keyword

    def do_GET(self):
        keyword = self.get_keyword()
        if not keyword:
            self.respond_json({"error": "Keyword not found"}, 400)
            return

        print(keyword)
        
        self.respond_json(scrape_item_from_tokped(keyword[0]))
        

if __name__ == "__main__":
    server_address = ("0.0.0.0", 5000)
    httpd = HTTPServer(server_address, SearchHandler)
    httpd.serve_forever()
