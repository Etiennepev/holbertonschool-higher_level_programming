#!/usr/bin/python3
"""
The module `request`
"""
import http.server
import json


class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleRequestHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
