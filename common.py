# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:00:10 2021

@author: Admin
"""

import pymysql
from pymysql.cursors import DictCursor

# 打开数据库连接
db = pymysql.connect(host="localhost",port=3306,user="linmon",passwd="linmon@123",db="game")
def db_fetchone(sql,msg=''):
    try:
        cursor = db.cursor(DictCursor)   
        cursor.execute(sql)
        data=cursor.fetchone()
    except Exception as e:
        print(msg)
        print("sql查询失败:")
        print(sql)
    else:
        return data
    
def db_fetchall(sql,msg=''):
    try:
        cursor = db.cursor(DictCursor)   
        cursor.execute(sql)
        data=cursor.fetchall()
    except Exception as e:
        print(msg)
        print("sql查询失败:")
        print(sql)
    else:
        return data    