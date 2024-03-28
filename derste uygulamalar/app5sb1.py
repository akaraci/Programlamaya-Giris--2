# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:37:44 2024

@author: akara
"""
#%% String->Ummutable->Değişmez
name="Ahmet"
#name[0]="S" #Hata
newname="S"+name[1:]
print(newname)

nameList=["Ahmet","Ayşe"]
nameList[0]="değişti mi?"
print(nameList)
#%%-->ShallowCopy
cities=["Samsun",61,"Ordu",52,"Ankara",6]
newCities=cities

print("id cities:",id(cities))
print("id newCities:",id(newCities))

print("cities:",cities)
print("newCities:",newCities)

newCities[1]=55

print("cities:",cities)
print("newCities:",newCities)

print("-"*40)

#newCitiesShallow=cities[:] #Method-1 for shallow copy
import copy
newCitiesShallow=copy.copy(cities) #Method-2 for shallow copy

print("id cities:",id(cities))
print("id newCitiesShallow:",id(newCitiesShallow))

newCitiesShallow[0]="İstanbul"
print("cities:",cities)
print("newCitiesShallow:",newCitiesShallow)

#%%




#%% DeepCopy
l=[["Ankara","İstanbul","Samsun"],[6,34,55],100,500,600]
print(l)
newl=l[:] #shallowcopy

print("id l=",id(l))
print("id newl=",id(newl))

print("id l[0]=",id(l[0]))
print("id newl[0]=",id(newl[0]))

print("-"*40)
newl[0][0]="Sinop"
newl[2]=90000

print("l=",l)
print("newl=",newl)

print("-"*40)
import copy
newldeep=copy.deepcopy(l) #apply deep copy
newldeep[0][1]="Sivas"
newldeep[3]=5500
print("l=",l)
print("newldeep=",newldeep)



#%%
#%%%
def double(liste):
    for index,value in enumerate(liste):
        liste[index]=2*value


numberList=[2,4,6,8]
print("Fonsiyondan önce:",numberList)
#double(numberList)
double(numberList[:]) #shallowcopy
print("fonksiyondan sonra:",numberList)





#%%
def double(liste):
    newList=[]
    for index,value in enumerate(liste):  
        newList.append(2*value)
    return newList

numberList=[2,4,6,8]
print("Fonsiyondan önce:",numberList)
#double(numberList)
print("Fonksiyondan dönen değer:",double(numberList))
print("fonksiyondan sonra:",numberList)

#%% Nested List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for value in row:
        print(value,end="\t")
    print()

for row in matrix:
    print(row)

#%% Liste Kavraması

nl=[1,2,3,4,-5,-10]

# newNumber=list(map(lambda x:x**2,nl))
# print(newNumber)

newNumber=[x**2 for x in nl]
print(newNumber)

newNumber1=[x**2 for x in nl if (x>0)]
print(newNumber1)
#%%
name=["Ali","Ayşe","Ahmet","Mustafa"]
age=[90,10,25,5]

newList=[nm for i,nm in enumerate(name) if (age[i]>18) ]
print(newList)


liste = [1, 2, 3, 4]
yeniliste2=[(x, x**2, x**3) for x in liste]
print(yeniliste2)

sayilar=[2,3]
harfler = ['a', 'b', 'c']
newharfler=[n*harf for n in sayilar for harf in harfler]
print(newharfler)












