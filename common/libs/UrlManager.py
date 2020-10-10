# 对url进行统一管理

import time
from application import app

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver="%s"%(int(time.time()))
        path="/static"+path+"?ver="+ver
        return UrlManager.buildUrl(path)

