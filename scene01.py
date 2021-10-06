# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 02:03:32 2021

@author: Admin
"""
import pymysql
from tkinter import *
from linmon import linmon,skill
from common import db_fetchone
from linmonFrame import linmonFrame
from game_core import game_core


def quit0(ui,gc):
    print('系统退出')
    gc.close()
    ui.destroy()

if __name__=='__main__':
    root=Tk()
    root.geometry('800x300')
    root.title('linmon')
    
    gb1=linmon(1)
    panel1=linmonFrame(root,gb1)
    
    gb2=linmon(2)
    panel2=linmonFrame(root,gb2)
    
    gc=game_core(gb1,gb2)
    gc.start()
    
    panel1.grid(row=0, column=0,rowspan=5,columnspan=7)
    panel2.grid(row=0, column=10,rowspan=5,columnspan=7)
    Button(root,text='开始',command=gc.close, width = 8).grid(row=0, column=7,columnspan=2)
    Button(root,text='关闭',command=gc.close, width = 8).grid(row=1, column=7,columnspan=2)
    
    root.protocol("WM_DELETE_WINDOW", lambda:quit0(root,gc))
    root.mainloop()