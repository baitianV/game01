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

def func(a):
    b=a
    b.type='2'

def fund(a):
    b=a
    b=3

a=linmon(1)
a.show()
func(a)
a.show()


b=1
fund(b)
print(b)
