# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 00:21:08 2021

@author: Admin
"""

def skill_01(sponsor):
    pass

def skill_02(sponsor,target):
    damage=sponsor.base_attack(1,2,'ap')
    target.base_suffer(damage)

def skill_03(sponsor,target):
    damage=sponsor.base_attack(1,1.5,'ap')
    target.base_suffer(damage)    
    
skill_all={
    1:skill_01,
    2:skill_02,
    3:skill_03
    }