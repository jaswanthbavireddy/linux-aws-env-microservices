import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class ProductHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            data = {"service": "product-service", "status": "healthy"}
        elif self.path in ("/", "/products"):
            status = 200
            data = {
                "service": "product-service",
                "version": "v1",
                "products": [
                    {"id": 1, "name": "Sample Product", "price": 199}
                ]
            }
        else:
            status = 404
            data = {"error": "Not found"}

        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), ProductHandler)
    print("Product Service listening on port 8000", flush=True)
    server.serve_forever()
