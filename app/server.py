"""hello — bee 첫 실모듈의 echo 서버 (표준 라이브러리만, 의존성 0)."""
import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080


class Echo(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "module": "hello",
            "env": os.environ.get("BEE_ENV", "unknown"),
            "host": socket.gethostname(),
            "path": self.path,
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}")


if __name__ == "__main__":
    print(f"hello listening :{PORT}")
    HTTPServer(("", PORT), Echo).serve_forever()
