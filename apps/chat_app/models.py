#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/27 16:26
from exct import db
from werkzeug.security import generate_password_hash,check_password_hash
import shortuuid

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    username = db.Column(db.String(50))
    _password = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)

    def check_pwd(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result