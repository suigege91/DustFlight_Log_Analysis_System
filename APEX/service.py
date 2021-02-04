from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

from application import DF_Tornado_Application

define("SERVER_PORT", default=9001,
       help="[CONSOLE] Process Running at SERVER_PORT Now...")
define("SERVER_HOST", default="127.0.0.1",
       help="[CONSOLE] Process Running at SERVER_HOST Now...")


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
    try:
        options.parse_command_line()
        http_server = HTTPServer(DF_Tornado_Application())
        http_server.listen(options.SERVER_PORT, options.SERVER_HOST)
        print(
            "[NOTICE] Development server is running at http://%s:%s" % (options.SERVER_HOST, options.SERVER_PORT))
        print("[NOTICE] Quit the server with Control-C")
        IOLoop.instance().start()
    except Exception as ex:
        print("[INVALID] Process Running Invalid [REASON] =>>>> [%s]" % str(ex))
    finally:
        print("[CONSOLE] DustFlight Tornado System Process Running Complete !")


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
