"""
视图处理类
"""
import simplejson as json
import sqlalchemy
from tornado.web import RequestHandler, authenticated

from . import models
from . import ModelsManager


u_m = ModelsManager.UserManager()
c_m = ModelsManager.CommentManager()
t_m = ModelsManager.TopicManager()


class BaseHandler(RequestHandler):
    """
    所有视图处理类的基础类
    """
    def get_current_user(self):
        user = self.get_cookie("login_user")
        if user:
            return True
        else:
            return False

    # def set_default_headers(self):
    #     self.set_header('Access-Control-Allow-Origin', '*')
    #     self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    #     self.set_header('Access-Control-Max-Age', 1000)
    #     self.set_header('Access-Control-Allow-Headers', '*')
    #     # self.set_header('Content-type', 'application/json')


class IndexHandler(BaseHandler):

    @authenticated
    def get(self):
        try:
            content = t_m.find_all()
            print(type(content))
            for x in content:
                print(x.title)
            return self.render("index.html", topic=content)
        except:
            return self.render("index.html", topic="还没有新动态呢~~~小主快去发布啦~~")


class LoginHandler(BaseHandler):

    def get(self):
        self.set_cookie("_xsrf", "DeX6gkqZjzElerQYwr7TH", expires_days=None)
        return self.render("login.html")

    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        # 数据库查询
        try:
            res = u_m.find_single(username, password)
            # res = u_m.DBSession().query(user).filter(sqlalchemy.and_(user.username==username, user.password==password)).one()
            self.set_cookie("login_user", username, expires_days=None)
            return self.write(json.dumps({"status": 1}))
        except Exception as e:
            # print(e)
            return self.write(json.dumps({
                "status": 0,
                "msg": "用户名或密码错误！！！"
            }))


class RegisterHandler(BaseHandler):

    def get(self):
        self.set_cookie("_xsrf", "DeX6gkqZjzElerQYwr7TH", expires_days=None)
        return self.render("register.html")

    def post(self):
        # self.set_default_headers()
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        confirmpsw = self.get_body_argument("confirmpsw")
        print(username, password, confirmpsw)
        if password == confirmpsw:
            try:
                # 入库操作
                user = models.User(username=username, password=password)
                u_m.create_obj(user)
                return self.write(json.dumps({
                    "status": 1,
                    "msg": ""
                }))
            except Exception as e:
                print(e)
                return self.write(json.dumps({
                    "status": 0,
                    "msg": "账号已存在，请重新尝试..."
                }))
        else:
            return self.write(json.dumps({
                "status": 0,
                "msg": "用户名或密码错误，请重新尝试..."
            }))


