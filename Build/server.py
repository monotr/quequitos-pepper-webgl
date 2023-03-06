import http.server
import socketserver

PORT = 5420

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
