#%%
a=10
print(a)
print(type(a))


#%% String Tanımlama
#ad="Ahmet"
# ad='Ahmet "Adres:bbbb"'
# ad="Ahmet \"Adres:bbbb\""
ad="Ahmet 'Adres:bbbb'"
print(ad)

print("""Bugün
      hava
          soğuk ya da sıcak???""")
print("yan\nyana mı\nyazar???")

#%% Print Command Usage
a=10
b=5
print(a," ile",b," nin çarpımı=",a*b)
print("%d ile %d nin çarpımı=%d"%(b,a,a*b))
print("{1} ile {0} nin çarpımı={2}".format(a,b,a*b))
print(f"{a} ile {b} nin çarpımı={a*b}")
#%%
for i in range(1,100,1):
    #print("%10d"%(i))
    print(f"{i:10}")
#%% usage end and sep parameter for print
# print("Merhaba Dünya",end=".")
print("Merhaba",end="--")
print("Dünya")

#sep->seperate
print("Bugün","hava","güzel",sep="-")
print("www","samsun","edu","tr",sep=".")
print(*"Dünya",sep=".")
print(*"Dünya",sep="\n")
#%%Input external data----Tip dönüşümü
while(1):
    try:
        vize=int(input("Vize="))
        final=int(input("Final="))
    except:
        print("Lütfen rakam girin")
    else:
        ort=vize*0.4+final*0.6
        print(f"Ortalama={ort}")
        break
#%%
try:
    a=int(input("a="))
    b=int(input("b="))
    bolum=a/b
except(ZeroDivisionError):
    print("b sıfır olmamalı")
except(ValueError):
    print("Rakam girin")
else:print(bolum)





#%%




















#%%

