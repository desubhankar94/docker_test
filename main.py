import http.server
import socketserver
import time
import os

count = 0
myhost = os.uname()[1]
dockerized = False
if os.path.isfile('/.dockerenv'):
    dockerized = True

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global count
        global myhost
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        curr_time = time.localtime()
        curr_clock = time.strftime("%H:%M:%S", curr_time)
        print(curr_clock)
        count = count + 1

        html = f"<html><head></head><body><h1>Hello World!</h1></body>" \
               f"<h2>Server Time: {curr_clock}</h2>" \
               f"<h2>Visitor Count: {count}</h2>" \
               f"<h2>Hostname: {myhost}</h2>" \
               f"<h2>App_is_dockerized: {str(dockerized)}</h2>" \
               f"</html>"
        self.wfile.write(bytes(html, "utf8"))
        return

handler_object = MyHttpRequestHandler
PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server.serve_forever()