#! /usr/bin/python
# coding: utf-8

import SimpleHTTPServer
import SocketServer
import os
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()
        self.wfile.write('function FindProxyForURL(url, host) { return "PROXY 192.168.100.1:8080; DIRECT"; }')
    def log_message(self, format, *args):
        return
def start():
    web_dir = os.path.join(os.path.dirname(__file__), 'web')
    os.chdir(web_dir)
    httpd = HTTPServer(('', 7070), MyHandler)
    httpd.serve_forever()
