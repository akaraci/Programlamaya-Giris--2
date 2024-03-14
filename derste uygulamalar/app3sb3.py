#%%
name="Ahmet"
# print(name[0])
# print(name[2:])
# print(name[:2])
# print(name[-1])
# print(name[:-1])
# print(name[::-1])
# print(name[-4:-2])
print(name(2:len(name)))

#%%
message="Merhaba"
for i in range(len(message)):
    print(i,message[i],sep="-")

print()

for i,ch in enumerate(message):
    print(i,ch,sep="-")



#%%
prefixes = "JKLMNOPQ"
suffix = "ack"
for ch in prefixes:
    #print(ch,suffix,sep="")
    print(ch+suffix)

#%%
password=input("Parola girin:")
if (password.lower()=="abc".lower()):
    print("Parola doğru")
else:print("parola yanlış")
#%%
message="Nerhaba"
#message[0]="M" #hata ->immutable object
message="M"+message[1:]
print(message)
#%%
def sesli_cikar(str):
    vowels = "aeioöuüAEIOÖUÜ"
    newstr=""
    for ch in str:
        if (ch not in vowels): #if (not ch in vowels)
            newstr+=ch
    return newstr

sesli_cikar("Merhaba")
#%%
def sesli_cikar(str):
    vowels = "aeioöuüAEIOÖUÜ"
    for item in vowels:
        str=str.replace(item,"") 
    return str

sesli_cikar("Merhaba")
#%%
def findIndex(str,ch):
    finded=[]
    for index,k in enumerate(str):
        if (k==ch):finded.append(index)
    if (len(finded)>0):return finded
    else:return -1

findIndex("Merhaba","a")
    
#%%
def count(str,ch):
    number=0
    for k in str:
        if (k==ch): number+=1
    return number

print(count("Merhaba","a"))

#%%
import string
x=string.ascii_letters
print(type(x),x)

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

#%%
import string
while(True):
    name=input("Input name:")
    control=True
    for ch in name:
        if (ch not in string.ascii_letters):
            print(ch,"Yanlış karakter")
            control=False
            #break
    if (control):break
print("Name true")

#%%
import string
def isLower(ch):
    if (ch in string.ascii_lowercase):
        return True
    else:return False

print(isLower("a"))
print(isLower("A"))
print(isLower("ç"))
#%%
from PIL import Image
im = Image.open("img.jpeg")
W, H = im.size # genislik, yukseklik
r, g, b = im.split() # RGB split
pr, pg, pb = r.load(), g.load(), b.load()
for x in range(W):
    for y in range(H):
        if pr[x, y] < 128:
            pr[x, y] = 0
        else:
            pr[x, y] = 255

        pg[x, y] = 255 - pg[x, y]
        pb[x, y] = pb[x, y] * 2

im2 = Image.merge("RGB", (r, g, b))
im2.show()
im2.rotate(45).show()
im.show()

#%%

















