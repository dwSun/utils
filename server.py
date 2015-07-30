import sys
import locale
import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("0.0.0.0", 80), handler)
httpd.serve_forever()