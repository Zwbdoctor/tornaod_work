"""
视图处理类
"""
import simplejson as json
from tornado.web import RequestHandler

from example.example import models
from example.example.example import ModelsManager

u_m = ModelsManager.UserManager()
c_m = ModelsManager.CommentManager()
t_m = ModelsManager.TopicManager()


class BaseHandler(RequestHandler):
    """
    所有视图处理类的基础类
    """
    def get_current_user(self):
        user = self.get_secure_cookie("login_user")
        if user:
            return True
        else:
            return False


class IndexHandler(BaseHandler):

    def get(self):
        return self.render("index.html")


class LoginHandler(BaseHandler):

    def get(self):
        return self.render("login.html")

    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("passwrod")
        print(username, password)
        # 数据库查询
        try:
            # 查询操作
            pass
        except Exception as e:
            print(e)
            return self.write({"msg": "用户名或密码错误..."})


class RegisterHandler(BaseHandler):

    def get(self):
        return self.render("register.html")

    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        confirmpsw = self.get_body_argument("confirmpsw")
        print(username, password, confirmpsw)
        if password == confirmpsw:
            try:
                # 入库操作
                user = models.User(username=username, pass_wd=password)
                u_m.create_obj(user)
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


