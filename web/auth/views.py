 # -*- coding: utf-8 -*-

import tornado.web
from db.mysql import dbconnector
from web.auth.forms import SignupForm,SigninForm

class LoginRequiredHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class signin(tornado.web.RequestHandler):
    def get(self):
        form = SigninForm()
        self.render("auth/signin.html",form=form)
    def post(self):
        user = {"username":self.get_argument('username'),
                "password":self.get_argument('password')}
        form = SigninForm()
        form.fillData(user)
        if form.validate():
            db = dbconnector().db
            cuser = db.get('select * from t_user where username="%s"'%(user["username"]))
            if cuser and cuser.password == user["password"]:
                self.set_secure_cookie("user", user["username"])
                self.redirect("/")
                return
            else:
                form.errors.append("用户名或密码错误")
        self.render("auth/signin.html",form=form)

class signup(tornado.web.RequestHandler):
    def get(self):
        form = SignupForm()
        self.render("auth/signup.html",form=form)
    def post(self):
        user = {"username":self.get_argument('username'),
                "email":self.get_argument('email'),
                "password":self.get_argument('password'),
                "repassword":self.get_argument('repassword')}
        form = SignupForm()
        form.fillData(user)
        if form.validate():
            db = dbconnector().db
            cuser = db.get('select * from t_user where username="%s"'%(user["username"]))
            if not cuser:
                insertsql = "INSERT INTO t_user (username,email,password) VALUES ('%s','%s','%s')"%(user["username"],user["email"],user["password"])
                rel = db.execute(insertsql)
                self.set_secure_cookie("user", user["username"])
                self.redirect("/")
                return
            else:
                form.errors.append("用户%s已存在!"%user["username"])
        self.render("auth/signup.html",form=form)

class logout(LoginRequiredHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")