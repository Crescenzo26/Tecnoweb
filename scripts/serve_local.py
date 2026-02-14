import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(ROOT, "site")


def main() -> None:
    os.chdir(SITE_DIR)
    host = "127.0.0.1"
    port = 8000
    print(f"Server avviato su http://{host}:{port}")
    ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler).serve_forever()


if __name__ == "__main__":
    main()
