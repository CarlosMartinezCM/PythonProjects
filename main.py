# Python 3 Web server example 
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

hostName = "localhost"
serverPort = 8081

myList = ['item 1, item 2, item 3']

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        #if the path ends with /myList it will run the code below
        if self.path.endswith('/myList'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            output = ''
            output += '<html><head><title>My List</title><head>'
            output += '<body>'
            output += '<p>This is an example web server.</p>'
            output += '<p>Still learning what this is actually doing.</p>'
            output += '<h2><a href="/myList/new">Add new item</h2>'
            for task in myList:
                output += task
                output += '</br></br>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        #if the path ends with /new it will run the code below
        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h2>Add new items<h2>'

            output += '<form method="POST" enctype="multipart/form-data" action="/myList/new">'
            output += '<input name="task" type="text" placeholder="Add new Item">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

        def do_POST(self):
            if self.path.endswith('/new'):
                content_ty, p_dict = cgi.parse_header(self.headers.get('content-type'))
                if content_ty == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, p_dict)
                    new_task = fields.get('task')
                    myList.append(new_task)

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.end_headers('Location', '/myList')
                self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName,serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName,serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server")

