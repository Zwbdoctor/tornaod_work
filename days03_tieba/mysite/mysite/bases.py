"""
项目基础模块定义
"""
import tornado.web

from . import settings
from . import urls


class BaseHandler(tornado.web.RequestHandler):
    pass



class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(urls.urlpatterns, **settings.settings)
