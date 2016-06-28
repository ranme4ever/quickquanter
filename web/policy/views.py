import tornado.web

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("policy/policy.html")
        pass