
#%%
from keyword import *
print(kwlist)
print(iskeyword("print"))
#%%
import keyword
print(keyword.kwlist)
#%%
import keyword as kw
print(kw.kwlist)
#%%
from keyword import kwlist
print(kwlist)
#print(iskeyword("print")) #hata

#%%
# from modul1sb1 import *
# lst=[2,4,6,8]
# lst1=kare(lst)
# print(lst1)

# lst2=kup(lst)
# print(lst2)

#%%
import modul1sb1 as m1
lst=[2,4,6,8]
lst1=m1.kare(lst)
print(lst1)

#%%
from m2sb1 import *
from m3sb1 import * #bu geçerli
print(question)
print(answer)

#%%% İki modülden de veri almak için
import m2sb1 as m2
import m3sb1 as m3
print(m2.question)
print(m2.answer)

print(m3.question)
print(m3.answer)


#%%%
import string
il="Samsun ÜNİVERSİTESİ"
print(il.upper())
print(string.capwords(il))
print(string.ascii_letters)

#%%







#%%%

















