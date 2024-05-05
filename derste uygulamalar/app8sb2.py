# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:41:19 2024

@author: akara
"""
#%%
class Nokta:
    #contructor (kurucu) metod
    def __init__(self,a=0,b=0):
        self.x=a #attribute
        self.y=b
        self.__hidden=5 #encapsulation (private variable)
    def noktalari_yaz(self,objectname):
        print(objectname,"(x,y)=(",self.x,",",self.y,")")
          
    def gizli_attribute_yaz(self):
        print("__hidden=",self.__hidden)
    
    def set_gizli_attribute(self,c):
        if (c<0):
            raise ValueError("Negatif değer hatası")
        else:self.__hidden=c
        
p1=Nokta()
#print(p1.__hidden) #hata
print(p1.x)
print(p1.gizli_attribute_yaz()) #get method
p1.set_gizli_attribute(-500) #set method
print(p1.gizli_attribute_yaz()) #get method


#%%
class Personel:
    def __init__(self,name="",surname="",maas=0):
        self.name=name
        self.surname=surname
        self.maas=maas
    def personel_bilgisi_yaz(self):
        print("%s %s personelinin maaşı=%d TL"%(self.name,self.surname,self.maas))

p1=Personel("Ahmet","aaa",5000)
p1.personel_bilgisi_yaz()

p2=p1 #shallow copy
p2.name="Mehmet"
p1.personel_bilgisi_yaz()
print(p1==p2)

import copy
p3=copy.deepcopy(p1)
p3.name="Ayşe"
p3.personel_bilgisi_yaz()
p1.personel_bilgisi_yaz()
print(p1==p3)




#%%


#%%









