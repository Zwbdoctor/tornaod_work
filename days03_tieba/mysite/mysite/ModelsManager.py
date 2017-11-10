"""
模型管理类
"""
from . import settings, models
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import pymysql
pymysql.install_as_MySQLdb()


class BaseModel(object):

    def __init__(self):
        self.create_engine = sqlalchemy.create_engine(settings.mysql_db, echo=True)
        self.DBSession = sessionmaker(bind=self.create_engine)

    def create_obj(self, args):
        """增加数据"""
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

    def update_obj(self, instance, **rules):
        """更新数据"""
        DB = self.DBSession()
        try:
            DB.query(instance).filter(**rules).update(synchronize_session=True)
            return True
        except Exception as e:
            print(e)
            DB.rollback()
            return False
        finally:
            DB.close()

    def delete_obj(self, instance, **rule):
        """删除数据"""
        DB = self.DBSession()
        try:
            DB.query(instance).filter(**rule).delete(synchronize_session=True)
        except Exception as e:
            return e
        finally:
            DB.close()


class UserManager(BaseModel):
    """用户管理类"""
    def find_single(self, *args):
        """查询单个"""
        DB = self.DBSession()
        user = models.User
        try:
            res = DB.query(user).filter(sqlalchemy.and_(user.username==args[0], user.password == args[1])).one()
            return res
        except Exception as e:
            return e
        finally:
            DB.close()

    def find_all(self, user):
        """查询所有"""
        DB = self.DBSession()
        user = models.User
        try:
            res = DB.query(user).all()
            return res
        except Exception as e:
            return e
        finally:
            DB.close()



class TopicManager(BaseModel):
    """帖子管理类"""
    def find_single(self, sql, params):
        """查询单个"""
        DB = self.DBSession()
        try:
            res = DB.execute(sql, params)
        except Exception as e:
            return e
        finally:
            DB.close()

    def find_all(self):
        """查询所有"""
        DB = self.DBSession()
        topic = models.Topic
        try:
            res = DB.query(topic.title).all()
            return res
        except Exception as e:
            return e
        finally:
            DB.close()


class CommentManager(BaseModel):
    """评论管理类"""
    def find_single(self, sql, params):
        """查询单个"""
        DB = self.DBSession()
        try:
            res = DB.execute(sql, params)
        except Exception as e:
            return e
        finally:
            DB.close()

    def find_all(self, instance, **rule):
        """查询所有"""
        DB = self.DBSession()
        try:
            res = DB.execute(instance, **rule)
            return res
        except Exception as e:
            return e
        finally:
            DB.close()

