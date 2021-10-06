# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 02:18:28 2021

@author: Admin
"""
import pymysql
from tkinter import *
from linmon import linmon,skill,command,damage
from common import db_fetchone
from linmonFrame import linmonFrame
from threading import Thread
import time
import queue


class game_core(Thread):
    
    def __init__(self,ui,gb1,gb2):
        super().__init__()
        self.command_queue=queue.Queue()
        self.ui=ui
        gb1.sign='gb1'
        gb2.sign='gb2'
        gb1.set_VSdata(self.command_queue,gb2.id)
        gb2.set_VSdata(self.command_queue,gb1.id)
        
        self.gb_all={
            gb1.id:gb1,
            gb2.id:gb2
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
                self.command_read(command)
                self.ui.update()
            self.core_time+=1
            
    def command_read(self,command):
        sponsor=self.gb_all[command.sponsor]
        target=self.gb_all[command.target]
        command.content(sponsor,target)
        sponsor.show()
        target.show()
            
           
    def close(self):
        self.quit_flag=True
                
        
if __name__=='__main__':
    pass
    # gc=game_core()
    # gc.start()
    # gc.time=3
    # gc.quit_flag=True
        