from web.auth.views import LoginRequiredHandler
import notebook.services.kernels.handlers as notebook_handlers
from notebook.base.handlers import APIHandler

class ShutDownKernel(APIHandler):
    def post(self,kernel_id):
        km = self.kernel_manager
        km.shutdown_kernel(kernel_id)
        self.finish()

handlers =  [
    (r"/api/kernels/shutdown/%s"%notebook_handlers._kernel_id_regex, ShutDownKernel),
]
handlers.extend(notebook_handlers.default_handlers)


