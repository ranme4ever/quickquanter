
class User():
    def __init__(self,request):
        self.username = request.get_argument('username')
        self.password = request.get_argument('pwd')
        self.email = request.get_argument('email')
        self.repwd = request.get_argument('repwd')
        pass
    def validate(self):
        errors = []
        self.checkUsername()
        self.checkEmail()
        self.checkPassword()
        return errors
    def checkUsername(self):
        if not self.username:
            errors.append({field:'username',error:'username is required'})
        if len(self.username)<=5:
             errors.append( {field:'username',error:'username is too short'})
    def checkEmail(self):
        pass

    def checkPassword(self):
        if not self.password == self.repwd:
            errors.append( {field:'password',error:'please input password again'})
