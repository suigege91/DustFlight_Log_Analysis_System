import os
import pymongo

from router import urls
from tornado.web import Application


class DF_Tornado_Application(Application):
    def __init__(self):
        settings = dict(
            debug=True,
            # xsrf_cookies=True,
            # login_url='/login',
            cookie_secret='#DustFlight_LAS#',
            static_path=os.path.join(os.path.dirname(__file__), "./static"),
            template_path=os.path.join(
                os.path.dirname(__file__), "./templates"),
        )

        conn = pymongo.MongoClient(host="localhost", port=27017)  # 连接 MongoDB
        self.db = conn["blog"]
        Application.__init__(self, handlers=urls, **settings)
