# # encoding:utf-8
# # __author__ = 'donghao'
# # __time__ = 2019/1/26 11:27
# import os,json
#
# DATA_DIR = os.path.dirname(__file__)+'/data/'
#
# class FileObj(object):
#     def __init__(self,filename):
#         self.filename = filename
#     def write(self,words):
#         with open(self.filename, 'a+', encoding='utf-8') as f:
#             f.write(words)
#
#     def file_lines(self):
#         count = 0
#         try:
#             thefile = open(self.filename, 'r', encoding='utf-8')
#         except Exception as e:
#             thefile = open(self.filename, 'a+', encoding='utf-8')
#         while True:
#             buffer = thefile.read(1024 * 8192)
#             if not buffer:
#                 break
#             count += buffer.count('\n')
#         thefile.close()
#         return count
#
#     def to_list(self):
#         index_messages = []
#         with open(self.filename, 'r', encoding='utf-8') as f:
#             for line in f.readlines():
#                 index_messages.append(line)
#         return index_messages
#
# file_index = 0
#
# file = FileObj(os.path.join(DATA_DIR,'messages_%d.txt'%file_index))
#
# while file.file_lines()>100:
#     file_index += 1
#     file = FileObj(os.path.join(DATA_DIR,'messages_%d.txt'%file_index))
#
# file.write(json.dumps({'username': '董浩', 'time': '2019/1/27'}, ensure_ascii=False) + '\n')
#
# messages_list = []
# for index in range(file_index+1):
#     file = FileObj(os.path.join(DATA_DIR, 'messages_%d.txt' % index))
#     messages_list+=file.to_list()
#
# import re
# from apps.chat_app.models import UserModel
# from chatroom import create_app
# app = create_app()

# with app.test_request_context():
#     logined_userid = ['dnL24hUKFzkYA7gxytLuA5','fxcGVFLWdAjQFrtV6hCicK','ktYzcHZc3jECa3U6nAskv6','wXFUrbRT7PjUrHw79rxarS']
#     users = [UserModel.query.get(user_id) for user_id in logined_userid]
#     for user in users:
#         print(user.username)
from operator import itemgetter
content = [
    {"username": "董浩", "msg": "1223", "create_time": "2019-01-28 10:31:48"},
    {"username": "董浩", "msg": "haha", "create_time": "2019-01-28 10:32:55"},
    {"username": "董浩", "msg": "aaa", "create_time": "2019-01-28 10:47:09"},
    {"username": "董浩", "msg": "haha", "create_time": "2019-01-28 10:40:03"},
    {"username": "董浩", "msg": "asdf", "create_time": "2019-01-28 10:15:56"},
    {"username": "董浩", "msg": "asdf*#emo_50#*", "create_time": "2019-01-28 10:25:59"},
    {"username": "董浩", "msg": "haha", "create_time": "2019-01-28 10:46:23"},
]

sorted_list = sorted(content,key=itemgetter('create_time'),reverse=True)
