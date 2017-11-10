"""
模型管理类
"""
import pymysql
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from example.example.example import settings

pymysql.install_as_MySQLdb()


class BaseModel(object):

    def __init__(self):
        self.create_engine = sqlalchemy.create_engine(settings.mysql_db, echo=True)
        self.DBSession = sessionmaker(bind=self.create_engine)

    def create_obj(self, args):
        DB = self.DBSession()
        try:
            DB.add(args)
            DB.commit()
            return True
        except Exception as e:
            print(e)
            DB.rollback()
            return False
        finally:
            DB.close()

    def update_obj(self, args):
        DB = self.DBSession()
        try:
            DB.add(args)
            return True
        except Exception as e:
            print(e)
            DB.rollback()
            return False
        finally:
            DB.close()




class UserManager(BaseModel):
    """用户管理类"""
    pass


class TopicManager(BaseModel):
    """帖子管理类"""
    pass


class CommentManager(BaseModel):
    """评论管理类"""
    pass

