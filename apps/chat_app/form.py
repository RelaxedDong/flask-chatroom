#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/27 18:22
from wtforms import StringField
from wtforms import Form
from wtforms.validators import Length,InputRequired

class Login_Register_Form(Form):
    password = StringField(validators=[Length(min=6,max=10,message='密码为6-10个字符~'),InputRequired(message='请输入密码')])
    username = StringField(validators=[InputRequired(message='请输入用户名')])