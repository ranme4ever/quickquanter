#-*- coding:utf-8 -*-
import tornado.web
from db.mysql import dbconnector
from web.auth.models import User
from web.auth.forms import SignupForm
class signin(tornado.web.RequestHandler):
    def get(self):
        self.render("auth/signin.html")

class signup(tornado.web.RequestHandler):
    def get(self):
        form = SignupForm()
        self.render("auth/signup.html",form=form)
    def post(self):
        user =  User(self)
        form = SignupForm()
        form.fillData(user)
        if form.validate():
            db = dbconnector().db
            user = db.get('select * from t_user where username="%s"'%(user.username))
            if not user:
                insertsql = "INSERT INTO t_user (username,email,password) VALUES ('%s','%s','%s')"%(user.username,user.email,user.password)
                rel = db.execute(insertsql)
                self.write(str(rel))
                return
            else:
                form.errors.append("user %s already is exists!"%user.username)
        self.render("auth/signup.html",form=form)

class logout(tornado.web.RequestHandler):
    def get(self):
        pass