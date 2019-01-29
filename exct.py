#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/26 11:03

from flask_wtf import CSRFProtect
from flask_socketio import SocketIO,emit,send
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()
db = SQLAlchemy()
socketio = SocketIO(async_mode=None,server='127.0.0.1')