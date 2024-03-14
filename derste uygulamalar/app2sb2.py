# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:37:55 2024

@author: akara
"""
#%%
def delete(mylist,item):
    if (type(item) is int):
        del mylist[item]
    else:
        mylist.remove(item)

list=[1,2,3,4,"5","deneme"]
print(type(list))
print(list[1])

delete(list,1)
print(list)

delete(list,"deneme")
print(list)

#%%
list1=[5,6,7,True,"55"]
list2=list1
print(id(list1),id(list2))
list2[0]="değişti mi?"
print("list1=",list1)
print("list2=",list2)

a=10
b=a
print(a,b)
b=33333
print(a,b)



#%%
#print("Senden"," "*10,"ç","o"*20,"k uzağım")
print(5*"Başlık  ")
print(40*"=")
#%%
x=10
print(id(x))
print(id(10))

#%%

# vize,final=60,90

# if(vize>50 and final>50):
#     print("geçti")

value=5
# if(value>=0 and value<=9):
#     print("rakam girdiniz")

if(9>=value>=0):
    print("rakam girdiniz")
#%%
password="abcd"
value=input("passwod'ü girin=")
if (password.lower()==value.lower()):
    print("Şifre doğru")
else:
    print("Şifre yanlış")
#%%
def print_square_root(x):
    if x <= 0:
        print ("Sadece pozitif sayılar lütfen.")
        # return
    else:
        result = x**0.5
        print ("x’in kare kökü=", result)

print_square_root(-144)
print_square_root(144)
#%%
def sor():
    response=input("Devam mı?(y,ye,ye,n,no,NO)=")
    if (response in ("y","ye","yes","Y","YES")):
        print("devam edilecek")
    elif (response in("n","N","no","NO","No")):
        print("devam edilmeyecek")

sor()

#%%
name=input("input to your name=")
# if (name==""):
#     print("Boş geçemezsiniz")

# if(not name):
#     print("Boş geçemezsiniz")

if(not bool(name)):
    print("Boş geçemezsiniz")
    

#%%











