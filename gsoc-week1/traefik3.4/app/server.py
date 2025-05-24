from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Python HTTP Server!")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 5000), SimpleHandler)
    print("Server started on http://localhost:5000")
    server.serve_forever()
