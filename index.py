#coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from flag import flag
from tornado.options import define,options
define("port",default=8080,type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_query_argument('user', default=None)
        code = self.get_query_argument('code', default=None)
        source = self.get_query_argument('source', default=None)
        if user == 'admin' and int(code) ^ 87788 == 0x15ff1:
        	self.write('hello,admin\n')
        	self.write(flag())
        else:
        	if source == '1':
        		with open('index.py','r') as file:
        			self.write(file.read())
        	else:
        		self.write('hello,user')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()