import torndb

class dbconnector():
    def __init__(self):
        self.db = torndb.Connection("127.0.0.1","db_quickquant","root")
    def db(self):
        return self.db