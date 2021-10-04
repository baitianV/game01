# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:51:48 2021

@author: Admin
"""
from tkinter import *
import pymysql
from pymysql.cursors import DictCursor

from linmon import linmon
from linmonFrame import linmonFrame
from common import db


sql="""
    SELECT TYPE,NATURE,C_MAX_HP,C_MAX_MP,C_HP,
    C_MP,C_ATK,C_DEF,C_INT,C_RES,C_SPD,C_SPR 
    FROM V_C_LINMON
    WHERE ID={}
""".format(1)

cursor = db.cursor(DictCursor)   
cursor.execute(sql)
data=cursor.fetchall()
print(data)