from handler import MainHandler, UserLoginHandler, UserLogoutHandler, UserRegisHandler, HomeHandler, DataRequireHandler, \
    DisplayHandler, ConsoleHandler

urls = [
    (r'/', MainHandler),
    (r'/home', HomeHandler),
    (r'/index', MainHandler),
    (r'/login', UserLoginHandler),
    (r'/regis', UserRegisHandler),
    (r'/logout', UserLogoutHandler),
    (r'/data_require', DataRequireHandler),
    (r'/display', DisplayHandler),
    (r'/console', ConsoleHandler),
]
