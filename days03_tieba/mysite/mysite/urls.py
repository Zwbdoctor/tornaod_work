"""
项目路由
"""
from . import views

urlpatterns = [
    (r'/', views.IndexHandler),
    (r'/register', views.RegisterHandler),
    (r'/login', views.LoginHandler),
]