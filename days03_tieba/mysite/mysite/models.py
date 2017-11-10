"""
用户类
"""
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


# 创建对象的基类
Base = declarative_base()


class User(Base):

    # 表名
    __tablename__ = "users"

    # 定义用户属性
    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    username = Column(sqlalchemy.VARCHAR(20), nullable=False)
    password = Column(sqlalchemy.VARCHAR(100), nullable=False)

    topics_id = relationship("Topic", backref("user"))
    # comment_id = relationship("comments", backref("users"))


class Topic(Base):
    __tablename__ = "topic"

    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    title = Column(sqlalchemy.VARCHAR(255))
    content = Column(sqlalchemy.TEXT)

    author = Column(sqlalchemy.INTEGER,
                    sqlalchemy.ForeignKey(column="user_id", _constraint="users", ondelete="CASCADE"),
                    nullable=False)
    # comment_id = relationship("Comments", backref("topic"))

"""
class Comments(Base):
    __tablename__ = "comments"

    id = Column(sqlalchemy.INTEGER,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    content = Column(sqlalchemy.TEXT)

    author = Column(sqlalchemy.INTEGER,
                    sqlalchemy.ForeignKey(column="user_id", _constraint="users", ondelete="CASCADE"),
                    nullable=False)
    title = Column(sqlalchemy.INTEGER,
                   sqlalchemy.ForeignKey(column="topic_id", _constraint="topic", ondelete="CASCADE"),
                   nullable=False)
"""

