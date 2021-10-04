# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 02:18:28 2021

@author: Admin
"""
import pymysql
from tkinter import *
from linmon import linmon,skill
from common import db_fetchone
from linmonFrame import linmonFrame
from threading import Thread
import time

class command(object):
    def __init__(self,sponsor,target,content,msg):
        self.sponsor=sponsor
        self.target=target
        self.content=content
        self.msg

#class content_read(object):

class game_core(Thread):
    
    def __init__(self,gb1,gb2):
        super().__init__()
        self.gb1=gb1
        self.gb2=gb2
        self.core_time=0
        self.quit_flag=False

    def run(self):
        self.core_time=0
        while self.quit_flag==False and i<5:
            command=self.command_queue.get(block=True)
            print(self.command.msg)
            time.sleep(2)
            self.core_time+=1
            
    def close(self):
        self.quit_flag=True
                
        
if __name__=='__main__':
    gc=game_core()
    gc.start()
    gc.time=3
    gc.quit_flag=True
        