from common.field import Field

class Form(object):
    def __init__(self):
        self.errors=[]

    def fields(self):
        fs = []
        for k,v in vars(self).items():
            if isinstance(v,Field):
                fs.append((k,v))
        return fs

    def validate(self):
        success = True
        for k,field in self.fields():
            success = field.validate() and success
        return success

    def fillData(self,data):
        for k,field in self.fields():
            if data.has_key(k):
                field.setValue(data[k])
