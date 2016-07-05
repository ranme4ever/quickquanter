#-*- coding:utf-8 -*-
import tornado.web
from web.auth.views import LoginRequiredHandler
from db.mysql import dbconnector
from web.policy.forms import RuleForm

class Rule(LoginRequiredHandler):
    @tornado.web.authenticated
    def get(self,rule_id=None):
        db = dbconnector().db
        username = tornado.escape.xhtml_escape(self.current_user)
        user = db.get("select id from t_user where username='%s'"%username)
        rules = db.query("select * from t_rule where user_id=%s"%user["id"])
        if not rules:
            rules = []
        crule = None
        if rule_id:
            crule = db.get("select * from t_rule where id=%s"%rule_id)
        self.render("policy/policy.html",rules=rules,crule=crule)

class RuleCreate(LoginRequiredHandler):
    def getUser(self,db):
        username = tornado.escape.xhtml_escape(self.current_user)
        user = db.get("select id from t_user where username='%s'"%username)

        return user
    def getRules(self,db,userid):
        return db.query("select * from t_rule where user_id=%s"%userid)

    @tornado.web.authenticated
    def get(self):
        form =RuleForm()
        db = dbconnector().db
        user = self.getUser(db)
        rules = self.getRules(db,user["id"])
        if not rules:
            rules = []
        self.render("policy/create.html",form=form,rules=rules)
        pass
    def post(self):
        form = RuleForm()
        rule = {"name":self.get_argument("name"),
                "desc":self.get_argument("desc")}
        form.fillData(rule)
        if form.validate():
            db = dbconnector().db
            cuser = self.getUser(db)
            crule = db.get("select * from t_rule where name='%s' and user_id='%s'"%(rule['name'],cuser['id']))
            if not crule:
                ruleid = db.execute("INSERT INTO t_rule (name,description,user_id) VALUES ('%s','%s','%s')"%(rule['name'],rule['desc'],cuser['id']))
                self.redirect("/policy/rule/%s"%ruleid)
                return
            else:
                form.errors.append("规则已存在")
        self.render("policy/create.html",form=form,rules=rules)