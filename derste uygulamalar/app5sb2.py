# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:26:31 2024

@author: akara
"""
#%%
name="Istanbul" #string ummutable -> değişmezdir
#name[0]="İ"
print(name)
#%% reference type and shallowcopy-Sığ Kopyalama
cities=["Samsun",34,"Ordu",52,"Ankara",6]
newCities=cities
print("Id cites",id(cities))
print("Id newCites",id(newCities))

newCities[1]=55
print("cities=",cities)
print("newCities=",newCities)

#-----shallow copy
#newCitiesShallow=cities[:] #method-1 for shallow copy
import copy
newCitiesShallow=copy.copy(cities) #method-2 for shallow copy

print("Id cites",id(cities))
print("Id newCitesShallow",id(newCitiesShallow))

print("-"*40)
newCitiesShallow[4]="Sinop"
print("cities=",cities)
print("newCitiesShallow=",newCitiesShallow)

#%% shallowcopy vs. deepcopy
l=[["Ankara","İstanbul","Samsun"],[6,34,55],100,500,600]
newl=l[:] #shallow

print("ID l=",id(l))
print("ID newl=",id(newl))

print("*"*30)
print("ID l[0]",id(l[0]))
print("ID newl[0]",id(newl[0]))

print("*"*30)
newl[0][1]="Sinop"
newl[2]=1500
print("newl=",newl)
print("l=",l)

#Deep Copy
import copy
newldeep=copy.deepcopy(l)
print("*"*30)
print("ID l[0]",id(l[0]))
print("ID newldeep[0]",id(newldeep[0]))

print("*"*30)
newldeep[0][2]="Ordu"
newldeep[2]=5500
print("newldeep=",newldeep)
print("l=",l)

#%%
def double(liste):
    for index,value in enumerate(liste):
        liste[index]=value**2

numberList=[2,4,6,8]
print("Fonksiyondan Önce numberList",numberList)
#double(numberList)
double(numberList[:])
print("Fonksiyondan Sonra numberList",numberList)   

    

#%%
#%%
def double(liste):
    newList=[]
    for index,value in enumerate(liste):
        newList.append(value**2)

numberList=[2,4,6,8]
print("Fonksiyondan Önce numberList",numberList)
double(numberList)
print("Fonksiyondan Sonra numberList",numberList) 
#%% Nested List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[2][2])

for row in matrix:
    for value in row:
        print(value,end="\t")
    print()
print("*"*30)
for row in matrix:
    print(row)
#%% Liste Kavraması
li=[2,4,6,8,-10,-20,-30]
#using map and lambda
kareli=list(map(lambda x:x**2,li))
print(kareli)

#Liste kavraması
kareli1=[x**2 for x in li]
print(kareli1)

pozitifkareli=[x**2 for x in li if x>0]
print(pozitifkareli)

number=[2,3]
ch=["a","b","c"]
complexList=[c*n for n in number for c in ch]
print(complexList)


#%% Liste kavraması örnek
name=["Ahmet","Ayşe","Ali","Mehmet"]
age=[25,5,10,45]
oldList=[nm for i,nm in enumerate(name) if (age[i]>18)]
print(oldList)


#%%















