# encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/26 11:27
import os,json
from flask import current_app
import config

file_index = 0

class FileObj(object):
    def __init__(self,filename):
        self.filename = filename
    def write(self,words):
        with open(self.filename, 'a+', encoding='utf-8') as f:
            f.write(words)

    def file_lines(self):
        count = 0
        try:
            thefile = open(self.filename, 'r', encoding='utf-8')
        except Exception as e:
            thefile = open(self.filename, 'a+', encoding='utf-8')
        while True:
            buffer = thefile.read(1024 * 8192)
            if not buffer:
                break
            count += buffer.count('\n')
        thefile.close()
        return count

    def to_list(self):
        index_messages = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    index_messages.append(eval(line.strip()))
        except Exception as e:
            print(e)
        finally:
            return index_messages

