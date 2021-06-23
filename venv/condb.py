# -*- coding = utf-8 -*-
# @Time : 2021-6-22 10:47
# @Author : GMZ
# @File : test.py
# @software : PyCharm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship  #创建关系
from config import DB_URI
from sqlalchemy.sql import func, literal_column #调用函数实现汉字首字母排序

engine = create_engine(DB_URI)  # 创建引擎
# conn = engine.connect()  # 连接
# result = conn.execute('SELECT 1')  # 执行SQL
# print(result.fetchone())
# conn.close()  # 关闭连接
Base = declarative_base(engine) # SQLORM基类
session =sessionmaker(engine)() # 构建session对象

#创建表login,储存用户名密码
class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    uid = Column(Integer)

#创建表student,学生基础信息
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(10))
    sex = Column(String(5))
    age = Column(Integer)
    classId = Column(Integer)
    score = relationship("Score", backref="score")

#创建班级表
class Class(Base):
    __tablename__ = 'class'
    cid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(10))

#教师表
class Teacher(Base):
    __tablename__ = 'teacher'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    tname = Column(String(10))

#课程表
class Course(Base):
    __tablename__ = 'course'
    cid = Column(Integer, primary_key=True, autoincrement=True)
    cname = Column(String(10))
    teacherId = Column(Integer, ForeignKey("teacher.tid"))
    score = relationship("Score", backref="courseName")

#成绩表
class Score(Base):
    __tablename__ = 'score'
    sid = Column(Integer, primary_key=True, autoincrement=True)
    studentId = Column(Integer, ForeignKey("student.id"))
    courseId = Column(Integer, ForeignKey("course.cid"))
    number = Column(Integer)

Base.metadata.create_all()  # 将模型映射到数据库中

#添加stuinfor表数据
def addStudnet(name,age,sex,classId):
    student = Student(name=name, age=age, sex=sex,classId=classId)
    session.add(student)  # 添加到session
    session.commit()  # 提交到数据库

#添加login表数据
def addLogin(username,password):
    login = Login(username=username, password=password)
    session.add(login)  # 添加到session
    session.commit()  # 提交到数据库

#整表遍历，输出整个student表
def searchStudent():
    return session.query(Student).all()

#表的单独列遍历，查询学生名单
def searchStudentNamelist():
    return session.query(Student.name).all()

#条件搜索，搜索年龄大于等于18的学生
def searchAge18():
    return session.query(Student).filter(Student.age >= 18).all()


#按照姓名排序,汉字首字母排序。
def orderByName():
    return session.query(Student).order_by(func.CONVERT(literal_column('name using gbk'))).all()
    #ession.query(Student).order_by(func.CONVERT(literal_column('name using gbk')).desc()).all()   desc()为倒序

#查询每个学生的各科成绩,通过外键关联,实现跨表查询
def searchScore():
    list = session.query(Student).all()
    for item in list:
        print(item.name)
        for i in item.score:
            courseObj = session.query(Course).filter_by(cid=i.courseId).first() #通过搜索获取的数据，进行精准查询
            print(courseObj.cname, i.number)
        print("-------------")
    return 0

searchScore()
