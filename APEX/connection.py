from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'DustFlight_LAS'
USERNAME = 'root'
PASSWORD = '1q2w3e4r!@#'
URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE
)
engine = create_engine(URL)
Base = declarative_base(bind=engine)
Session = sessionmaker(engine)
session = Session()
