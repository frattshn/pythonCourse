#Girilecek kelimeyi girilecek sayı kadar ekrana bastıran kod.
def EkranaYazdir(kelime, adet):
    print(kelime*adet)
EkranaYazdir('Merhaba\n', 10)

#Kendisine girilen sınırsız sayıdaki bilgiyi listeye ekleyen kod.
def liste(*args):
    liste=[]
    for i in args:
        liste.append(i)
    return liste
result=liste(10, 20, "araba")
print(result)

#Girilen iki sayı arasındaki asal sayıları ekrana basan kod.

def asalSayiBul(sayi1, sayi2):
    for i in range(sayi1, sayi2+1):
        if i>1:
            for j in range(2,i):
                if (i%j==0):
                    break
            else:
                print(i)

sayi1=int(input("1.sayı: "))
sayi2=int(input("2.sayı: "))

asalSayiBul(sayi1,sayi2)


#Sayının tam bölenlerini bulan kod.

def tambolenbul(sayi):
    TamBolen=[]

    for i in range(2,sayi):
        if sayi%i==0:
            TamBolen.append(i)
    return TamBolen
print(tambolenbul(20))











