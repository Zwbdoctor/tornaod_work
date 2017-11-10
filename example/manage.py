"""
项目入口
"""
from tornado.ioloop import IOLoop
from tornado.options import options

# from bases import Application
import mysite.bases as bases

if __name__ == "__main__":
    app = bases.Application()
    app.listen(options.port)
    print("Server is starting...")
    IOLoop.current().start()