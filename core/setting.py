import os
from web import auth,api,home,policy
from notebook.services.kernels.kernelmanager import MappingKernelManager
from traitlets.config.configurable import SingletonConfigurable

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
module_handlers = [
    auth.handlers.handlers,
    api.handlers.handlers,
    home.handlers.handlers,
    policy.handlers.handlers,
]

setting = {
    "static_path": os.path.join(BASE_DIR, "static"),
    "template_path" : os.path.join(BASE_DIR, "templates"),
    "kernel_manager":MappingKernelManager(),
}

class Setting(SingletonConfigurable):
    def __init__(self):
        self.handlers = []
        self.settings = {}
        self.initSettings()
        self.initHandlers()

    def initHandlers(self):
        for module_handler in module_handlers:
            for handler in module_handler:
                self.handlers.append(handler)

    def initSettings(self):
        self.settings =setting

    @classmethod
    def handlers(cls):
        instance = cls.instance()
        return instance.handlers
    @classmethod
    def settings(cls):
        instance = cls.instance()
        return instance.settings

