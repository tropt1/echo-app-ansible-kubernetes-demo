import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        author = os.getenv("AUTHOR", "Bolotov Maxim")
        content = f"""
        <html><body>
          <h1>Echo Server</h1>
          <p>Hostname: {hostname}</p>
          <p>IP: {ip}</p>
          <p>Author: {author}</p>
        </body></html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())


if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Listening on port {PORT}...")
    server.serve_forever()

