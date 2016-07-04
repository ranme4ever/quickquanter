
class User():
    def __init__(self,request):
        self.username = request.get_argument('username')
        self.email = request.get_argument('email')
        self.password = request.get_argument('password')
        self.repassword = request.get_argument('repassword')
        pass