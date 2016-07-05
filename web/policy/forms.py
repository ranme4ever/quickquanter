#-*- coding:utf-8 -*-
from common.form import Form
from common.field import TextField

class RuleForm(Form):
    def __init__(self):
        self.name = TextField("规则名",30,True)
        self.desc = TextField("概述",64,False)