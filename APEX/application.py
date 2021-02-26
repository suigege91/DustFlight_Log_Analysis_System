import config

from router import urls
from tornado.web import Application


class DF_Tornado_Application(Application):
    def __init__(self):
        Application.__init__(self, handlers=urls, **config.settings)
