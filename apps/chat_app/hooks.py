#encoding:utf-8

from .views import bp
from flask import session,g
import config
from .models import UserModel

@bp.before_request
def before_request():
    if config.FRONT_USER_ID in session:
        user_id = session.get(config.FRONT_USER_ID)
        user = UserModel.query.get(user_id)
        if user:
            g.front_user_id = user.id
    else:
        g.front_user = ''






