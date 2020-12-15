"""
x =input("1.Sayi: ")  #İnput kodu kullanıcıdan değer ister.15
y =input("2.Sayi: ")

print(type(x))
print(type(y))
toplam= int(x) + int(y)
print(toplam)
"""

x = 5               #int
y = 5.8             #float
name = "Fırat"      #string
isOnline = True    #bool

"""
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))
"""

#Tip Dönüşümleri

#int to float

x=float(x)
print(x)
print(type(x))

y=int(y)
print(y)
print(type(y))

result= str(x) + str(y)
print(result)
print(type(result))

#bool to str

isOnline=str(isOnline)
print(isOnline)
print(type(isOnline))

isOnline=True

#bool to int

isOnline=int(isOnline)
print(isOnline)
print(type(isOnline))