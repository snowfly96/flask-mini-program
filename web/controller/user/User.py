# 定义用户视图蓝图
from flask import Blueprint,render_template,request,json,jsonify
from common.models.User import User
from common.libs.user.UserService import UserService

route_user=Blueprint("user_page",__name__)

# GET请求作为界面展示，POST作为提交请求
@route_user.route('/login',methods=["GET","POST"])
def login():
    if request.method=='GET':
        return render_template("user/login.html")
    # 请求状态
    resp={'code':200,'msg':'登陆成功','data':{}}
    print(resp)
    req=request.values
    login_name=req["login_name"] if "login_name" in req else None
    login_pwd=req["login_pwd"] if "login_pwd" in req else None

    if login_name==None or len(login_name)<1:
        resp['code']=-1
        resp['msg']='请输入正确的登陆用户名~~'
        return jsonify(resp)
    if login_pwd==None or len(login_pwd)<1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的登陆密码~~'
        return jsonify(resp)
    # 在数据库中查询登录用户名是否存在，并检测密码是否正确
    user_info=User.query.filter_by(login_name=login_name).first()
    if not user_info: # 用户不存在
        resp['code'] = -1
        resp['msg'] = '请输入正确的登陆用户名和密码 -1~~'
        return jsonify(resp)
    # 数据库中保存的是用户明文密码与加密字符串进行md5加密后的密码
    if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_pwd):
        resp['code'] = -1
        resp['msg'] = '请输入正确的登陆用户名和密码 -2~~'
        return jsonify(resp)
    # 登陆成功
    return resp


@route_user.route('/edit')
def edit():
    return render_template("user/edit.html")

@route_user.route('/reset-pwd')
def resetPwd():
    return render_template("user/reset_pwd.html")