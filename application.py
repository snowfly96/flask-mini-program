from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os

# 继承Flask
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path = None):
        super(Application,self).__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=None)
        # 加载配置文件（os.environ包含系统环境）//按照不同环境进行加载
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            # 通过export|set ops_config 将该环境导入系统环境中
            print(os.environ['ops_config'])
            self.config.from_pyfile('config/%s_setting.py'%os.environ['ops_config'])

        db.init_app(self)

db=SQLAlchemy()
# 使用template_folder重新定位模板文件
app=Application(__name__,template_folder=os.getcwd()+"/web/templates/",root_path=os.getcwd()) # 完成了应用的创建并添加配置文件到App,同时将应用绑定了数据库
manager=Manager(app) # 使用Manager对app进行包装

"""
将python的方法注入到HTML中进行使用
"""
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl")
app.add_template_global(UrlManager.buildUrl,"buildUrl")

