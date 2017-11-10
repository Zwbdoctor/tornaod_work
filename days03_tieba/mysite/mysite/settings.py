"""
项目配置文件
"""
from tornado.options import define
import os


define("port", default=8000, type=int)

BaseDir = os.path.dirname(__file__)

settings = {
    "template_path": os.path.join(BaseDir, "templates"),
    "static_path": os.path.join(BaseDir, "static"),
    "debug": True,
    "cookie_secret": "AZJIRCoFRDeX6+5gk/qZjzCjb0ZY9ElerQYwGrY7THw=",
    "xsrf_cookies": True,
    "login_url": "/login",
}

mysql_db = "mysql://root:root@localhost:3306/db_tornado"
