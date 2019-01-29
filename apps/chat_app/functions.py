#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/27 15:07
from utils.upload_message import FileObj
import config
import os
from operator import itemgetter
def get_all_messages():
    messages_list = []
    for file_name in os.listdir(config.DATA_DIR):
        file = FileObj(config.DATA_DIR+"\\"+file_name)
        messages_list+=file.to_list()
    return sorted(messages_list, key=itemgetter('create_time'))

