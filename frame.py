# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:38:36 2021

@author: Admin
"""
import pymysql
from tkinter import *
from linmon import linmon
db = pymysql.connect(host="localhost",port=3306,user="linmon",passwd="linmon@123",db="game")
root=Tk()
root.geometry('800x300')
root.title('linmon')


ob1=linmon(db,1)
ob1.show()

        

panel=LabelFrame(root,padx=1,pady=1)

#第一层
type_name=StringVar()
type_name.set(ob1.type)
Label(panel,textvariable=type_name).grid(row=0, column=0)

#第二层
nature=StringVar()
nature.set(ob1.nature)
Label(panel,text='属性：').grid(row=1, column=0)
Label(panel,textvariable=nature).grid(row=1, column=1)

#第三层
hp=StringVar()
hp.set(ob1.properties['hp'])
max_hp=StringVar()
max_hp.set(ob1.properties['max_hp'])
Label(panel,text='生命值：').grid(row=2, column=0)
Label(panel,textvariable=hp).grid(row=2, column=1)
Label(panel,text='/').grid(row=2, column=2)
Label(panel,textvariable=max_hp).grid(row=2, column=3)

#第四层
mp=StringVar()
mp.set(ob1.properties['mp'])
max_mp=StringVar()
max_mp.set(ob1.properties['max_mp'])
Label(panel,text='魔法值：').grid(row=3, column=0)
Label(panel,textvariable=hp).grid(row=3, column=1)
Label(panel,text='/').grid(row=3, column=2)
Label(panel,textvariable=max_hp).grid(row=3, column=3)

#第五层
c_atk=StringVar()
c_atk.set(ob1.properties['atk'])
Label(panel,text='物攻：').grid(row=4, column=0)
Label(panel,textvariable=c_atk).grid(row=4, column=1)
c_def=StringVar()
c_def.set(ob1.properties['def'])
Label(panel,text='物防：').grid(row=4, column=3)
Label(panel,textvariable=c_def).grid(row=4, column=4)

#第六层
c_int=StringVar()
c_int.set(ob1.properties['int'])
Label(panel,text='魔攻：').grid(row=5, column=0)
Label(panel,textvariable=c_int).grid(row=5, column=1)
c_ref=StringVar()
c_ref.set(ob1.properties['def'])
Label(panel,text='魔防：').grid(row=5, column=3)
Label(panel,textvariable=c_ref).grid(row=5, column=4)

#第7层
c_spd=StringVar()
c_spd.set(ob1.properties['spd'])
Label(panel,text='速度：').grid(row=6, column=0)
Label(panel,textvariable=c_spd).grid(row=6, column=1)
c_spr=StringVar()
c_spr.set(ob1.properties['spr'])
Label(panel,text='敏捷：').grid(row=6, column=3)
Label(panel,textvariable=c_spr).grid(row=6, column=4)



panel.grid(row=0, column=0,rowspan=5,columnspan=5)
db.close()
root.mainloop()   
