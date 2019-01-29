#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/27 16:00
from .views import bp

@bp.app_template_filter('content')
def filter_posts(value):
    result = value.replace("*#", "<img src='static/img/").replace("#*", ".gif'/>")
    return result