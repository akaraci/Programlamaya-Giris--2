#%%
while(True):   
    try:
        a=int(input("Bölünen Girin:"))
        b=int(input("Böleni Girin:"))
        print(a/b)
        break
    except ZeroDivisionError:
        print("Böleni sıfır girmeyin")
    except ValueError:
        print("Lütfen rakam girin")
    except:
        print("Bilinmeyen bir oluştu")
#%%
tup = ('a', 'b', 'd', 'e')
try:
    tup[2] = 'c'
except TypeError:
    print("Tupple değiştirilemez")
#%%
try: 
    a = [10,20,30]
    index=int(input("Kaçıncı Eleman:"))
    print (a[index])
except IndexError:
    print("Indeks Hatası oluştu")

#%%
filename="myfile2.txt"
try:
    file=open(filename,"r")
    notu=int(file.readline())
    print(notu)
except FileNotFoundError:
    print(f"{filename} dosyası bulunamadı")
except ValueError as err:
    errmsg=err.args
    print(errmsg)


#%%%
class Nokta:
    def __init__(self,a,b):
        self.x=a
        self.y=b
object1=Nokta(20,30)
object2=Nokta(50,100)
print(object1.x)
print(object1.y)
print(object2.x)
print(object2.y)
# print(type(Nokta))
# print(type(object1))
#%%

#%%


#%%



#%%
