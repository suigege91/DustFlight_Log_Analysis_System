import os
import pymongo

BASE_DIRS = os.path.dirname(__file__)
conn = pymongo.MongoClient(host="localhost", port=27017)
db = conn["blog"]

options = dict(
    SERVER_PORT=9001,
    SERVER_HOST="127.0.0.1",
    help="[CONSOLE] Process Running at SERVER_HOST Now...",
    list=[]
)

settings = dict(
    debug=True,
    autoreload=True,
    cookie_secret='#DustFlight_LAS#',
    static_path=os.path.join(BASE_DIRS, "./static"),
    template_path=os.path.join(BASE_DIRS, './templates'),
)

# options = {
#     "SERVER_PORT": 9001,
#     "SERVER_HOST": "127.0.0.1",
#     "help": "[CONSOLE] Process Running at SERVER_HOST Now...",
#     "list": []
# }
#
# settings = {
#     "debug": True,
#     "autoreload": True,
#     "cookie_secret": '#DustFlight_LAS#',
#     "static_path": os.path.join(BASE_DIRS, "./static"),
#     "template_path": os.path.join(BASE_DIRS, './templates'),
# }
