# 所有请求static文件下的东西都是经过该文件进行处理
from flask import Blueprint,send_from_directory
from application import app

route_static=Blueprint("static",__name__)

@route_static.route("/<path:filename>")
def index(filename):
    # 将http://127.0.0.1:8999/static/下请求的资源转到从http://127.0.0.1:8999/web/static/下获得
    # 解决加载资源问题,将指定文件发送到请求该文件的客户端
    return send_from_directory(app.root_path+"/web/static/",filename)