from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


SITE_ROOT = Path(__file__).resolve().parent


class CleanURLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        request_path = self.path.split("?", 1)[0].split("#", 1)[0]
        candidate = SITE_ROOT / request_path.lstrip("/")
        if request_path != "/" and not candidate.suffix and candidate.with_suffix(".html").is_file():
            suffix = self.path[len(request_path) :]
            self.path = f"{request_path}.html{suffix}"
        super().do_GET()


if __name__ == "__main__":
    handler = lambda *args, **kwargs: CleanURLHandler(*args, directory=str(SITE_ROOT), **kwargs)
    ThreadingHTTPServer(("", 3000), handler).serve_forever()
