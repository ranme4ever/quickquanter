#-*- coding:utf-8 -*-
from common.form import Form
from common.field import TextField,PasswordInput

class SignupForm(Form):
    def __init__(self):
        self.username = TextField("用户名",30,True)
        self.email = TextField("邮箱",30,True)
        self.password = PasswordInput("密码",20,True)
        self.repassword =  PasswordInput("确认密码",20,True)
        self.errors = []
    def fillData(self,data):
        for k,field in self.fields():
            if hasattr(data,k):
                field.set(getattr(data,k))

    def validate(self):
        success = True
        for k,field in self.fields():
            success = field.validate() and success
        if self.password.value != self.repassword.value:
            self.errors.append("两次密码输入不一致")
            success  = False
        return success



