import config

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options, parse_command_line, parse_config_file

from application import DF_Tornado_Application

define("charset", type=str)
define("SERVER_PORT", default=9001,
       help="[CONSOLE] Process Running at SERVER_PORT Now...", group="application")
define("SERVER_HOST", default="127.0.0.1",
       help="[CONSOLE] Process Running at SERVER_HOST Now...", group="application")


def application_start():
    print("=========================================================")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("#########################################################")
    service_core_running()
    print("[NOTICE] Running Function => [tornado_engine_start] Complete !")
    print("#########################################################")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("=========================================================")


def service_core_running():
    import os
    BASE_DIRS = os.path.dirname(__file__)
    config_file = os.path.join(BASE_DIRS, "./config.py")
    # try:
    # options.parse_command_line()
    options.parse_config_file(config_file)
    http_server = HTTPServer(DF_Tornado_Application())
    # http_server.listen(options.SERVER_PORT, options.SERVER_HOST)
    http_server.bind(config.options.SERVER_PORT, config.options.SERVER_HOST)
    print(
        "[NOTICE] Development server is running at http://%s:%s" % (
            config.options.SERVER_HOST, config.options.SERVER_PORT))
    print("[NOTICE] Quit the server with Control-C")
    IOLoop.instance().start()
    # except Exception as ex:
    #     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    #     print("-----------------------------------------------------------------------------------")
    #     print("[INVALID] Process Running Invalid [REASON] =>>>> [%s]" % str(ex))
    #     print("-----------------------------------------------------------------------------------")
    #     print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # finally:
    #     print("[CONSOLE] DustFlight Tornado System Process Running Complete !")


def main():
    print("=========================================================")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("#########################################################")
    application_start()
    print("#########################################################")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("=========================================================")


if __name__ == '__main__':
    main()
