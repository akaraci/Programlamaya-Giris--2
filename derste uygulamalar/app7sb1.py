#%%
while(True):
    
    try:
        a=int(input("Bölüneni girin:"))
        b=int(input("Böleni girin:"))
        print(a/b)
        break
    except:print("bölen sıfır olamaz")

#%%%
while(True):
    
    try:
        a=int(input("Bölüneni girin:"))
        b=int(input("Böleni girin:"))
        print(a/b)
        break
    except ZeroDivisionError:print("bölen sıfır olamaz")
    except ValueError:print("Lütfen rakam giriniz!!!")

#%%
tup = ('a', 'b', 'd', 'e')
try:
    tup[2] = 'c'
except TypeError:print("Tupple'daki değer değiştirilemez. Liste kullanın")

#%%%
a = [10,0,30]
try:
    index=int(input("Kaçıncı Eleman:"))
    print (a[index])
    print(a[0]/a[1])
except IndexError:print("Indeksi doğru girin")
except ValueError:print("Indeksi rakam olarak girin")
except:print("Bilinmeyen hata oluştu")
#%%%
filename = input('Enter a file name: ')
try:
    f = open (filename, "r")
except:
    print ('There is no file named', filename)


#%%%%
try:
    f = open('myfile1.txt')
    s = f.readline()
    i = int(s.strip()) #boşlukları siler. Karakter ya da karakterler verilirse onları da siler.
    print(i)
except IOError as e:
    errno, strerror = e.args
    print ("I/O error({0}): {1}".format(errno, strerror))
except ValueError:
    print ("Could not convert data to an integer.")
except:
    print ("Unexpected error:")


#%%
age=int(input("Yaşınızı girin:"))
if age<0:
    raise ValueError("%s yaş değeri sıfırdan küçük"%age)
print("Yaşınız:",age)
#%%%
x = "hello"
if type(x) is not int:
  raise TypeError("Only integers are allowed")
#%%%
class Nokta:
    def __init__(self,a,b):
        self.x=a
        self.y=b

object1=Nokta(5,10) #instance
object2=Nokta(20,30) #instance

print(type(Nokta))
print(type(object1))

print("x=",object1.x)
print("y=",object1.y)

print("x=",object2.x)
print("y=",object2.y)



#%%%%



#%%%%

#%%


#%%

#%%

