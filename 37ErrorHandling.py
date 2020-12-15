
liste=["1","2","5a","10b","abc","10","50"]
new_list=[]

#Liste elemanları içindeki sayısal değerleri bulunuz.
"""
for x in liste:
    try:
        result=int(x)
        print(result)
        new_list.append(result)
    except ValueError:
        continue
print(new_list)
"""

#Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olun
#aksi halde hata mesajı yazın.
"""
while True:
    sayi= input("Sayı: ")
    if sayi=='q':
        print("Döngüden çıktınız..")
        break

    try:
        result= float(sayi)
        print("Girdiğiniz sayı: ", result)
        break
    except ValueError:
        print("Geçersiz Sayı...")
        continue
"""


#Girilen parola içinde Türkçe karakter hatası veriniz.
"""
def checkPassword(parola):
    turkce_karakterler="şŞçÇüÜğĞöÖıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola Türkçe karakter içeremez...")
        else:
            pass
    print("Geçerli parola...")

parola=input("Parola: ")



try:
    checkPassword(parola)
except TypeError as err:
    print(err)



"""

#Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları veriniz.
"""
def faktoriyel(x):
    x= int(x)

    if x<0:
        raise ValueError("Negatif değer giriniz...")

    result=1
    for i in range(1, x+1):
        result*=i
    return result

for j in [5,10,'12A',-3,6,-1]:
    try:
        y= faktoriyel(j)
    except ValueError as err:
        print(err)
        continue
    print(y)

"""


