"""
路由定义配置模块
"""
from example.example.example import views

urlpatterns = [
    (r"/", views.IndexHandler),
    (r"/login", views.LoginHandler),
]