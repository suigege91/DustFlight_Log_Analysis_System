from connection import Base
from sqlalchemy import Column, Integer, String


def application_start():
    create_db()
    print("[NOTICE] Running Function => [create_db] Complete !")
    # drop_db()
    # print("[NOTICE] Running Function => [drop_db] Complete !")


def create_db():
    try:
        Base.metadata.create_all()
        print("---------------------------------------------")
        print("#############################################")
        print("|||||||||||||||||||||||||||||||||||||||||||||")
        print("---------------------------------------------")
        print("[SUCCESS] Data Injection Successfully  !")
        print("---------------------------------------------")
        print("|||||||||||||||||||||||||||||||||||||||||||||")
        print("#############################################")
        print("---------------------------------------------")
    except Exception as ex:
        print("[INVALID] Data Injection Invalid  !" % str(ex))


def drop_db():
    try:
        Base.metadata.drop_all()
        print("---------------------------------------------")
        print("#############################################")
        print("|||||||||||||||||||||||||||||||||||||||||||||")
        print("---------------------------------------------")
        print("[SUCCESS] DB Dropping Successfully  !")
        print("---------------------------------------------")
        print("|||||||||||||||||||||||||||||||||||||||||||||")
        print("#############################################")
        print("---------------------------------------------")
    except Exception as ex:
        print("[INVALID] DB Dropping Invalid  !" % str(ex))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(16), primary_key=False,
                  unique=True, nullable=False)
    password = Column(String(32), primary_key=False,
                      unique=False, nullable=False)
    email = Column(String(64), primary_key=False,
                   unique=False, nullable=False)
    tel = Column(String(16), primary_key=False,
                 unique=False, nullable=False)
    address = Column(String(256), primary_key=False,
                     unique=False, nullable=False)


def main():
    print("--------------------------------------------------------------------")
    print("====================================================================")
    print("=================================[]=================================")
    application_start()
    print("=================================[]=================================")
    print("====================================================================")
    print("--------------------------------------------------------------------")


if __name__ == '__main__':
    main()
