
from jupyter_core.application import JupyterApp
from tornado import httpserver,web
from zmq.eventloop import ioloop
ioloop.install()
from core.setting import Setting

class MainApp(JupyterApp):
    def __init__(self):
        self.settings = Setting.settings()
        self.handlers = Setting.handlers()
        self.handlers.append((r"/(apple-touch-icon\.png)", web.StaticFileHandler, dict(path= self.settings['static_path'])),)
        self.setup()
        print "MainApp initalize complete"

    def setup(self):
        self.app = web.Application(self.handlers,**self.settings)
        self.http_server = httpserver.HTTPServer(self.app)

        self.http_server.listen(80, "127.0.0.1")
        #self.app.listen(80)
        self.ioloop = ioloop.IOLoop.current()


    def start(self):
        print "MainApp listened on port 80"
        self.ioloop.start()

    @classmethod
    def running(cls):
        instance = cls.instance()
        instance.start()

if __name__ =="__main__":
    MainApp.running()







