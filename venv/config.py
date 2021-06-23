# -*- coding = utf-8 -*-
# @Time : 2021-6-22 11:18
# @Author : GMZ
# @File : config.py
# @software : PyCharm

HOST = 'localhost'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'root123'
DB = 'stusystem'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'