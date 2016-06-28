import tornado.web
from db.mysql import dbconnector
from web.auth.models import User
class sigin(tornado.web.RequestHandler):
    def get(self):
        self.write("hello auth sigin")

class sigout(tornado.web.RequestHandler):
    def get(self):
        self.render("auth/signup.html")
    def post(self):
        user = new User(self)
        errors = user.validate()
        if len(errors)<=0:
            db = dbconnector().db;
            user = db.get('select * from t_user where username="%s"'%(username))
            if not user:
                insertsql = "INSERT INTO t_user (username,email,password) VALUES ('%s','%s','%s')"%(username,email,pwd)
                rel = db.execute(insertsql)
                self.write(str(rel))
                return
            else:
                errors.append("user %s is exists!"%username)
        self.render("auth/signup.html",errors)

class logout(tornado.web.RequestHandler):
    def get(self):
        pass