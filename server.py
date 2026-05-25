import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class HTMLRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map[''] = 'text/html'

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('0.0.0.0', 8000), HTMLRequestHandler)
    print('Serving on http://localhost:8000')
    server.serve_forever()
