from http.server import BaseHTTPRequestHandler, HTTPServer


class ControlPlaneHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"control-plane ok")


def start_http_server(host: str = "127.0.0.1", port: int = 8080) -> None:
    server = HTTPServer((host, port), ControlPlaneHandler)
    print(f"control-plane API listening on {host}:{port}")
    server.serve_forever()
