#-*- coding:utf-8 -*-
from common.form import Form
from common.field import TextField,PasswordInput

class SignupForm(Form):
    def __init__(self):
        super(SignupForm,self).__init__()
        self.username = TextField("用户名",30,True)
        self.email = TextField("邮箱",30,True)
        self.password = PasswordInput("密码",20,True)
        self.repassword =  PasswordInput("确认密码",20,True)

    def validate(self):
        success = super(SignupForm,self).validate()
        if self.password.value != self.repassword.value:
            self.errors.append("两次密码输入不一致")
            success  = False
        return success

class SigninForm(Form):
    def __init__(self):
        super(SigninForm,self).__init__()
        self.username = TextField("用户名",30,True)
        self.password = PasswordInput("密码",20,True)

    def validate(self):
        success = super(SigninForm,self).validate()
        return success



