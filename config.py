#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/26 10:58
import os

SECRET_KEY = 'hsjdflsajdf'
FRONT_USER_ID = 'jsaldjflsjd'
DATA_DIR = os.path.join(os.path.dirname(__file__),'data')

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'chatroom'

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
