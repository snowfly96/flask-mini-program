# 用户的统一核心操作
import hashlib,base64

class UserService():
    # 利用密码与加密字符串生成密码
    @staticmethod
    def genePwd(pwd,salt):
        m=hashlib.md5()
        str="%s-%s"%(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()