#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/26 11:02

from exct import socketio
from flask_socketio import emit,send
from apps.chat_app.views import logined_userid
import config
import os,json
from datetime import datetime
from utils.upload_message import FileObj,file_index
from apps.chat_app.models import UserModel
index = 0

def ack(value):
    #客户端传递
    print( value)


@socketio.on('send_message')
def handle_json(msg):
    global file_index
    user = UserModel.query.get(msg.get('send_id'))
    if user:
        return_msg = {
            'username':user.username,
            'msg':msg['data'],
            'create_time':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        file = FileObj(os.path.join(config.DATA_DIR, 'messages_%d.txt' % file_index))
        while file.file_lines() > 1500:
            file_index += 1
            file = FileObj(os.path.join(config.DATA_DIR, 'messages_%d.txt' % file_index))
        file.write(json.dumps(return_msg, ensure_ascii=False) + '\n')
        emit('recive_msg',return_msg,broadcast=True, callback=ack)



#新登陆用户
@socketio.on('newLogin')
def newLogin(username):
    user = UserModel.query.filter_by(username=username).first()
    if user.id not in logined_userid:
        logined_userid.append(user.id)
        emit('newLogin_return', username, broadcast=True)
    return 'success'


@socketio.on('newLogout')
def newLogout(user_id):
    user = UserModel.query.get(user_id)
    emit('newLogout_return',user.username,broadcast=True)
    return 'success'


# # 函数形式
# import json
# def return_json(data):
#     emit('return_json',json.dumps(data))
#
# socketio.on_event('return_json', return_json)