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
import queue

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
        self.command_queue=queue.Queue()
        
        gb1.sign='gb1'
        gb2.sign='gb2'
        gb1.set_VSdata(self.command_queue,gb2.id)
        gb2.set_VSdata(self.command_queue,gb1.id)
        
        self.gb_all={
            'gb1':gb1,
            'gb2':gb2
            }
        self.core_time=0
        self.quit_flag=False

    def run(self):
        self.core_time=0
        while self.quit_flag==False:
            try:
                command=self.command_queue.get(block=True)
            except queue.Empty:
                pass
            else:
                print(command.msg)
            self.core_time+=1
            
    def close(self):
        self.quit_flag=True
                
        
if __name__=='__main__':
    pass
    # gc=game_core()
    # gc.start()
    # gc.time=3
    # gc.quit_flag=True
        