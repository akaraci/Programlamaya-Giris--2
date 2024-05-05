#%%
myfile=open("info.dat","w")
print(myfile)
myfile.write("1. satır yazıldı")
myfile.write("\n2. satır yazıldı")
myfile.close()

myfile=open("info.dat","a")
myfile.write("\n3. satır yazıldı")
myfile.write("\n4. satır yazıldı")
myfile.close()


#%%%
myfile=open("info.dat","a")
myfile.write("\n5. satır yazıldı")
myfile.write("\n6. satır yazıldı")
myfile.close()
#%%%
try:
    myfile=open("info1.dat","r")
except FileNotFoundError:
    print("dosya bulunamadı!!!")

#%%
with open("info.dat","r") as myfile:
    text=myfile.read()
    print(text)
    print(type(text))
    myfile.close()

#%%
myfile=open("info.dat","r")
text=myfile.read(10) #10 karakter okur
print(text)

# myfile.close() #açıp kapatarak çıktıyı takip edin.
# myfile=open("info.dat","r")
text1=myfile.read()
print(text1)
myfile.close()

#%%%
myfile=open("info.dat","r")
line1=myfile.readline()
print(line1)
line2=myfile.readline()
print(line2)

alllines=myfile.readlines()
print(alllines)

for l in alllines:
    print(l,end="")


#%%


#%%%




#%%%




