#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/27 16:29
from exct import db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from run import create_app

app =  create_app()


from apps.chat_app import models


User = models.UserModel


manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.option('-u','--u',dest='username')
@manager.option('-p','--p',dest='password')
def add_user(username,password):
    user = User(username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('用户添加成功')


if __name__ == '__main__':
    manager.run()