def yaz(str):
    """Bu fonksiyon kendine gönderilen 
       parametreyi ekrana 5 defa yazar.
    """
    print(5*str)

yaz("Merhaba")


def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    False
    """
    print (n % 2 == 0 or n % 5 == 0)

print("name:",__name__)
if (__name__=='__main__'):
    import doctest
    doctest.testmod()
#%%
def is_divisible(x, y):
    #return x % y == 0
    return x % y
    # if (x%y==0): return True
    # else:return False

# print(is_divisible(10, 2))
# print(is_divisible(10, 4))

if (not is_divisible(10, 2)):print("bölünebilir")
else: print("bölünemez")


#%%
import matplotlib.pyplot as plt

plt.plot([10,100,100,10,10],[10,10,110,110,10])



#%%
import matplotlib.pyplot as plt
def dortgen_ciz(xstart,ystart,width,height):
    x=[xstart,xstart+width,xstart+width,xstart,xstart]
    y=[ystart,ystart,ystart+height,ystart+height,ystart]
    plt.plot(x,y)

dortgen_ciz(10, 10, 50, 150)
dortgen_ciz(20, 20, 30, 50)


#%% send function parameter to other function
def a(n):
    return 2*n

def b(n):
    return 2*n+1

def c(n):
    return n%2

def todo(n,function):
    print(function(n))

todo(5,a)
todo(20,c)
#%% default parameter for function
def sor(mesaj,hak=2,uyari="evet yada hayır"):
    while(True):
        cevap=input(mesaj)
        if (cevap in ("evt","evet")):return True
        elif (cevap in ("hyr","hayır")): return False
        print(uyari)
        hak-=1
        if (hak==0):
            print("bir türlü doğru giremediniz")
            break
    
    
#sor("cevabıbızı girin:")
sor("cevabıbızı girin:",3,"evt yada hyr şeklinde girin")


#%%
def addName(name,liste=[]):
    liste.append(name)
    print(liste)

addName("Eray")
addName("Kevser")
addName("Eslen")
#%% parameter with *
def sum(*numbers):
    print(numbers)
    print(type(numbers))
    toplam=0
    for number in numbers:
        toplam+=number
        print(number)
    return toplam
        

print("toplam=",sum(10,20,50,-5,20))

#%%
def showPerson(**info):
    print(info)
    print(type(info))
    keys=info.keys()
    print(keys)
    for key in keys:
        print(key,":",info[key])

showPerson(name="Eslen",age=19,job="student")



#%% using lambda

# def kare(n):
#     return n**2
# print(kare(5))

kare=lambda x:x**2

print(kare(9))

toplam=lambda x,y:x+y
print(toplam(8,10))
#%% filter for list
liste=[10,20,-50,-10,90,75]
newList=list(filter(lambda x:x>0, liste))
print(newList)

newList1=list(filter(lambda x:not x%2, liste))
print(newList1)
#%%











  

