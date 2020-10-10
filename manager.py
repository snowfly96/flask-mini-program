from application import app,manager
from flask_script import Server
import www

# 自定义运行命令
manager.add_command("runserver",Server(host='127.0.0.1',port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main()) # 存在任何错误退出编译器
    except Exception as e:
        import traceback
        traceback.print_exc() # 将所有错误打印出来