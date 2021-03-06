from http_transparent import *

class ThreadingHTTPSServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6
    daemon_threads = True

    cakey = 'ca.key'
    cacert = 'ca.crt'
    def get_request(self):
        request, client_address = self.socket.accept()
        #print help(self.socket)
        #print self.socket.getpeername()
        request = ssl.wrap_socket(request, keyfile=self.cakey, certfile=self.cacert, server_side=True)
        #print help(self)
        #print help(ssl)
        #raw_input()
        return request, client_address

    def handle_error(self, request, client_address):
        # surpress socket/ssl related errors
        cls, e = sys.exc_info()[:2]
        if cls is socket.error or cls is ssl.SSLError:
            pass
        else:
            return HTTPServer.handle_error(self, request, client_address)


def interception_https(HandlerClass=ProxyRequestHandler, ServerClass=ThreadingHTTPSServer, protocol="HTTP/1.1"):

    server_address = ('', 9090)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    #print "Serving HTTPS Proxy on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    interception_https()
