# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:23:56 2021

@author: Admin
"""
import pymysql
from tkinter import *
from linmon import linmon,skill
from common import db_fetchone

class linmonFrame(LabelFrame):
    
    
    def __init__(self,parent,gb):
        super().__init__(parent,padx=1,pady=1)
        self.gb=gb
        self.setUI()

    def setGB(self,id):
        return linmon(id)

    def setUI(self):
        #第一层
        type_name=StringVar()
        type_name.set(self.gb.type)
        Label(self,textvariable=type_name).grid(row=0, column=0)
        
        #第二层
        nature=StringVar()
        nature.set(self.gb.nature)
        Label(self,text='属性：').grid(row=1, column=0)
        Label(self,textvariable=nature).grid(row=1, column=1)
        
        #第三层
        hp=StringVar()
        hp.set(self.gb.properties['hp'])
        max_hp=StringVar()
        max_hp.set(self.gb.properties['max_hp'])
        Label(self,text='生命值：').grid(row=2, column=0)
        Label(self,textvariable=hp).grid(row=2, column=1)
        Label(self,text='/').grid(row=2, column=2)
        Label(self,textvariable=max_hp).grid(row=2, column=3)
        
        #第四层
        mp=StringVar()
        mp.set(self.gb.properties['mp'])
        max_mp=StringVar()
        max_mp.set(self.gb.properties['max_mp'])
        Label(self,text='魔法值：').grid(row=3, column=0)
        Label(self,textvariable=hp).grid(row=3, column=1)
        Label(self,text='/').grid(row=3, column=2)
        Label(self,textvariable=max_hp).grid(row=3, column=3)
        
        #第五层
        c_atk=StringVar()
        c_atk.set(self.gb.properties['atk'])
        Label(self,text='物攻：').grid(row=4, column=0)
        Label(self,textvariable=c_atk).grid(row=4, column=1)
        c_def=StringVar()
        c_def.set(self.gb.properties['def'])
        Label(self,text='物防：').grid(row=4, column=3)
        Label(self,textvariable=c_def).grid(row=4, column=4)
        
        #第六层
        c_int=StringVar()
        c_int.set(self.gb.properties['int'])
        Label(self,text='魔攻：').grid(row=5, column=0)
        Label(self,textvariable=c_int).grid(row=5, column=1)
        c_ref=StringVar()
        c_ref.set(self.gb.properties['def'])
        Label(self,text='魔防：').grid(row=5, column=3)
        Label(self,textvariable=c_ref).grid(row=5, column=4)
        
        #第7层
        c_spd=StringVar()
        c_spd.set(self.gb.properties['spd'])
        Label(self,text='速度：').grid(row=6, column=0)
        Label(self,textvariable=c_spd).grid(row=6, column=1)
        c_spr=StringVar()
        c_spr.set(self.gb.properties['spr'])
        Label(self,text='敏捷：').grid(row=6, column=3)
        Label(self,textvariable=c_spr).grid(row=6, column=4)
    
class skillButton(Button):
    def __init__(self,parent,skill):
        super().__init__(parent)
        self.skill=skill
        self.setUI()
        
    def setUI():
        super().config(text=self.skill.name,width = 8)
           
class skillFrame(LabelFrame):
    def __init__(self,parent,skill_list):
        super().__init__(parent)
        self.skill=skill
        self.gb.show()
        self.setUI()
        

if __name__=='__main__':
    root=Tk()
    root.geometry('800x300')
    root.title('linmon')
    gb=linmon(1)
    panel=linmonFrame(root,gb)
    panel.grid(row=0, column=0,rowspan=5,columnspan=7)
    root.mainloop()
    db.close()