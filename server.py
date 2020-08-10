from http.server import BaseHTTPRequestHandler, HTTPServer 
import http.server 


class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("ok".encode("utf-8"))
        
    def do_POST(self):
        post_body = self.rfile.read(int(self.headers['Content-Length']))
        RESPONSE = post_body
        print("Post message arrived\n"+str(RESPONSE))
        #LOGGER.debug("POST request Body:{}".format(str(post_body.decode('utf-8'))))
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Message arrived. Thank you".encode("utf-8"))
        #time.sleep(1)
        
def run(server_class=HTTPServer, handler_class=GetHandler, port=1234):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting http server on port {}..\n'.format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping http server...\n') 

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
