# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 02:36:40 2021

@author: Admin
"""
from common import db,db_fetchone,db_fetchall
from skill import skill_all

class damage(object):
    def __init__(self,val,dm_type):
        self.val=val
        self.dm_type=dm_type

class command(object):
    def __init__(self,sponsor,target,content,msg):
        self.sponsor=sponsor
        self.target=target
        self.content=content
        self.msg=msg
        
    def read(self):
        args=self.content.split('#')
        return args
        

class skill(object):
    def __init__(self,owner,id):
        sql="""
            SELECT ID,NAME,TYPE,METHOD,COST,DESCRIPTION,COLD,SPELL_TIME,
            RUN_TIME,REST_TIME,EFFECT,POINT
            FROM B_SKILL
            WHERE ID={}
        """.format(id)
        data=db_fetchone(sql)
        self.release=skill_all[id]
        self.owner=owner
        self.id=id
        self.name=data['NAME']
        self.type=data['TYPE']
        self.method=data['METHOD']
        self.cost=data['COST']
        self.description=data['DESCRIPTION']
        self.code=data['COLD']
        self.spell_time=data['SPELL_TIME']
        self.run_time=data['RUN_TIME']
        self.rest_time=data['REST_TIME']
        self.effect=data['EFFECT']
        self.point=data['POINT']
                
    def get_command(self):
        cm=command(self.owner.id,self.owner.enemy_id,self.release,self.name)
        return cm
    
    def add_skill_command(self):
        cm=self.get_command()
        self.owner.command_queue.put(cm)
    
class linmon(object):
    
    def __init__(self,id):
        sql="""
            SELECT TYPE,NATURE,C_MAX_HP,C_MAX_MP,C_HP,
            C_MP,C_ATK,C_DEF,C_INT,C_RES,C_SPD,C_SPR 
            FROM V_C_LINMON
            WHERE ID={}
        """.format(id)    
        data=db_fetchone(sql)
        self.id=id
        self.type=data['TYPE']
        self.nature=data['NATURE']
        self.properties={
            'max_hp':data['C_MAX_HP'],
            'max_mp':data['C_MAX_MP'],
            'hp':data['C_HP'],
            'mp':data['C_MP'],
            'atk':data['C_ATK'],
            'def':data['C_DEF'],
            'int':data['C_INT'],
            'res':data['C_RES'],
            'spd':data['C_SPD'],
            'spr':data['C_SPR']
        }
        self.skill_list=self.get_skill_list()
        self.sign=''
    
    def init_data(self):
        sql="""
            SELECT TYPE,NATURE,C_MAX_HP,C_MAX_MP,C_HP,
            C_MP,C_ATK,C_DEF,C_INT,C_RES,C_SPD,C_SPR 
            FROM V_C_LINMON
            WHERE ID={}
        """.format(id)    
        data=db_fetchone(sql)
        return data
    
    def get_skill_list(self):
        sql="""
            SELECT LINMON_ID,SKILL_ID,STATUS_ID
            FROM C_LINMON_SKILL
            WHERE LINMON_ID={}
            ORDER BY SKILL_ID
        """.format(self.id)    
        data=db_fetchall(sql)
        print(data)
        skill_list=[]
        for item in data:
            sk=skill(self,item['SKILL_ID'])
            skill_list.append(sk)
        return skill_list
    
    def set_VSdata(self,command_queue,enemy_id):
        self.command_queue=command_queue
        self.enemy_id=enemy_id
        
    def show(self):
        print('类型：',self.type)
        print('属性：',self.nature)
        for item in self.properties:
            tmp=''+item+':'+str(self.properties[item])+' '
            print(tmp,end='')
        print()
        
    def base_attack(self,base,coe,dm_type):
        if dm_type=='ad':          
            val=int(base+self.properties['atk']*float(coe))
        elif dm_type=='ap':
            val=int(base+self.properties['int']*float(coe))
        return damage(val, dm_type)
    
    def base_suffer(self,damage):
        self.properties['hp']=self.properties['hp']-damage.val
        
    def base_defense(self,damage):
        if damage.dm_type=='ad':
            damage.val=damage.val-self.properties['def']
        elif damage.val=='ap':
            damage.val=damage.val-self.properties['res']
        self.base_suffer(damage)
         
if __name__=='__main__':
    ln=linmon(1)
    sk=ln.skill_list[0].owner.type
    print(sk)
    
    print(ln.ad_attack(0.2, 3.8))
        