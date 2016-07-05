import tornado.web
from web.auth.views import LoginRequiredHandler

class index(LoginRequiredHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)
        self.render("index.html")
