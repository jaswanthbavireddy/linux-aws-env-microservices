import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class UserHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            data = {"service": "user-service", "status": "healthy"}
        elif self.path in ("/", "/users"):
            status = 200
            data = {
                "service": "user-service",
                "version": "v1",
                "users": [
                    {"id": 1, "name": "Sample User"}
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
    server = ThreadingHTTPServer(("0.0.0.0", 8000), UserHandler)
    print("User Service listening on port 8000", flush=True)
    server.serve_forever()
