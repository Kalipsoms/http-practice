
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 8765

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            directory=str(Path(__file__).resolve().parent),
            **kwargs
        )

    def do_POST(self):
        self.send_response(405)
        self.send_header("Allow", "GET, HEAD")
        self.end_headers()
        self.wfile.write(b"405 Method Not Allowed")


server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)

print(f"Сервер работает: http://127.0.0.1:{PORT}", flush=True)

server.serve_forever()
