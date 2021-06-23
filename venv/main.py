# -*- coding = utf-8 -*-
# @Time : 2021-6-22 3:25
# @Author : GMZ
# @File : main.py
# @software : PyCharm
import os
from flask import Flask,render_template,request,flash
import datetime
from flask_wtf import FlaskForm #wtf表单模块
from wtforms import StringField,PasswordField,SubmitField #wtf表单类型
from wtforms.validators import DataRequired,EqualTo #数据存在确认和对比模块
from flask_sqlalchemy import SQLAlchemy
import condb



app = Flask(__name__,
            template_folder="..\\templates")
app.secret_key = 'passwd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@127.0.0.1/stusystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#定义用户注册form表单
class registerForm(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    password0 = PasswordField('密码：',validators=[DataRequired()])
    password1 = PasswordField('确认密码：',validators=[DataRequired(),EqualTo("password0","密码输入不一致")])
    submit = SubmitField('提交')

#register,注册界面
@app.route('/register',methods=['GET','POST'])
def register():
    register = registerForm()
    if request.method == "POST":
        username = request.form.get('username')
        password0 = request.form.get('password0')
        password1 = request.form.get('password1')
        if register.validate_on_submit():
            condb.addLogin(username,password0)
            return "success"
        else:
            flash("参数有误")

    return render_template('register.html',register=register)

#主页
@app.route('/')
def mainPage():
    return render_template('mainpage.html')

#搜索
@app.route('/search')
def search():
    return render_template('search.html')






if __name__ == '__main__':
    app.run(debug=True)