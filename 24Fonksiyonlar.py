
print("=======================")

def sayHello():
    print("Hello World")
sayHello()

print("=======================")

def sayHi(name):
    print("Hello "+name)
sayHi("Fırat")

print("=======================")

def sayHel(name="UserName"):
    print("Hello "+name)
sayHel("Memduh")
sayHel()                          #Parametre belirtilmediği zaman otomatik olarak fonksiyonun içinde atama yazılır.

print("=======================")

def sayHell(name="UserName"):
    return "Hello "+name
msg=sayHell("Sivaslı")
print(msg)

print("=======================")

def total(num1,num2):
    return num1+num2
result=total(10,20)
print(result)

print("=======================")

def yasHesapla(dogumyili):
    return 2020-dogumyili
yasFirat=yasHesapla(2000)
yasAykut=yasHesapla(1993)
yasTugce=yasHesapla(1997)

print(yasFirat)
print(yasAykut)
print(yasTugce)

print("=======================")

def EmekliligeKacYilKaldi(dogumyili,isim):
    yas=yasHesapla(dogumyili)
    emeklilik=65-yas

    if emeklilik>0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı {isim} bey.")
    else:
        print("Zaten emeklisiniz.")
EmekliligeKacYilKaldi(1990,"Ali")