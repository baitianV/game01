# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 02:33:07 2021

@author: Admin
"""
from tkinter import *
import pymysql
from linmon import linmon
from linmonFrame import linmonFrame
from common import db

root=Tk()
root.geometry('800x300')
root.title('linmon')

panel=linmonFrame(root,db,1)
panel.grid(row=0, column=0,rowspan=5,columnspan=5)


panel_1=linmonFrame(root,db,2)
panel_1.grid(row=0, column=10,rowspan=5,columnspan=5)



root.mainloop()
db.close()