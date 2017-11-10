"""
用户类
"""
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .ModelsManager import TopicManager, UserManager, CommentManager


# 创建对象的基类
Base = declarative_base()


class User(Base):

    # 表名
    __tablename__ = "users"

    # 定义用户属性
    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True)
    username = sqlalchemy.VARCHAR(50)
    pass_wd = sqlalchemy.VARCHAR(100)

    topics_id = relationship("Topic")
    comment_id = relationship("Comment")


class Topic(Base):
    """
    贴吧帖子
    """
    __tablename__ = "topic"

    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True)
    title = Column(sqlalchemy.VARCHAR(255))
    content = Column(sqlalchemy.TEXT)

    author = Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey(column="user_id", _constraint="user", ondelete="CASCADE"))
    comment_id = relationship("comment")


class Comment(Base):
    """
    贴子评论
    """
    __tablename__ = "comments"

    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True)
    content = Column(sqlalchemy.TEXT)

    author = Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey(column="user_id", _constraint="user", ondelete="CASCADE"))
    title = Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey(column="topic_id", _constraint="topic", ondelete="CASCADE"))

