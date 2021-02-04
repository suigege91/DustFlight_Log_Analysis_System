import os

cmd = "python ./APEX/service.py"


def application_start():
    service_start(cmd)
    print("[NOTICE] Running Function => [service_start] Complete !")


def service_start(cmd):
    os.system(cmd)
    print("[CONSOLE] Running Terminal Executor Complete ! CMD => [%s]" % str(cmd))


def main():
    print("===========================================================")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    application_start()
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("===========================================================")


if __name__ == '__main__':
    main()
