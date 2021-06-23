# -*- coding = utf-8 -*-
# @Time : 2021-6-22 10:47
# @Author : GMZ
# @File : test.py
# @software : PyCharm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker
from config import DB_URI

engine = create_engine(DB_URI)  # 创建引擎
# conn = engine.connect()  # 连接
# result = conn.execute('SELECT 1')  # 执行SQL
# print(result.fetchone())
# conn.close()  # 关闭连接
Base = declarative_base(engine) # SQLORM基类
session =sessionmaker(engine)() # 构建session对象

#创建表stuinfor,学生基础信息
class Student(Base):
    __tablename__ = 'stuinfor'
    id = Column(Integer,primary_key=True)
    name = Column(String(10))
    sex = Column(String(5))
    age = Column(Integer)

#创建表login,储存用户名密码
class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    uid = Column(Integer, ForeignKey("stuinfor.id"))

Base.metadata.create_all()  # 将模型映射到数据库中

#添加stuinfor表数据
def addStudnet(name,age,sex,id):
    student = Student(name=name, age=age, sex=sex,id=id)
    session.add(student)  # 添加到session
    session.commit()  # 提交到数据库

#添加login表数据
def addLogin(username,password):
    login = Login(username=username, password=password)
    session.add(login)  # 添加到session
    session.commit()  # 提交到数据库
