class A(object):
    sa = "sa"
    def __init__(self):
        self.a = 1
        self.b = 2

    def test(self):
        for f,v in vars(self).items():
            print f,v
a = A()
a.test()
print dir(a)