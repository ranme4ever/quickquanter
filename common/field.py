#-*- coding:utf-8 -*-
class Field():
    def __init__(self):
        self.value = None
        pass
    def set(self,value):
        self.value = value

    def validate(self):
        return True

class TextField(Field):
    def __init__(self,label,max_length,required):
        self.label = label
        self.max_length = max_length
        self.required = required
        self.errors = []
        self.type = "text"
        pass

    def validate(self):
        self.errors=[]
        if self.required and len(self.value)<=0:
            self.errors.append("%s是必填项"%self.label)
            return False
        if len(self.value)>self.max_length:
            self.errors.append("%s超出最大长度%s"%(self.label,self.max_length))
            return False
        return True

class PasswordInput(Field):
    def __init__(self,label,max_length,required):
        self.label = label
        self.required = required
        self.max_length = max_length
        self.errors = []
        self.type = "password"
    def validate(self):
        self.errors = []
        if self.required and len(self.value)<=0:
            self.errors.append("%s是必填项!"%self.label)
            return False
        if self.value and len(self.value)>self.max_length:
            self.errors.append("%s超出最大长度%s"%(self.label,self.max_length))
            return False
        return True


