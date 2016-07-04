from common.field import Field

class Form(object):
    def fields(self):
        fs = []
        for k,v in vars(self).items():
            if isinstance(v,Field):
                fs.append((k,v))
        return fs
