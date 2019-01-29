`*

## A Chat Room Completed with Flask-socketio

`功能：`
 1. 实时消息更新，实时用户上线显示
 2. 快捷注册
 3. 快捷登陆
 4. 表情支持
 
`截图：`
![聊天界](https://img-blog.csdnimg.cn/20190129214414552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjM5NTIw,size_16,color_FFFFFF,t_70)

![标签支持](https://img-blog.csdnimg.cn/20190129214429986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjM5NTIw,size_16,color_FFFFFF,t_70)
`使用方法:`
1.  安装依赖：pip install -r requirements.txt
2. 数据库迁移，映射  
 `python manage.py db init`      
 `python manage.py db  migrate  `
 `python manage.py db upgrade`


**提示**: 聊天记录为了简化直接将  消息存储指data文件里面，文件格式为message_index.txt，如果文件行数大于记录大于1500，会自动新建文件
