import tornado.web

class index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
