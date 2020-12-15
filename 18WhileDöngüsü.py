
#Girilen iki değer arasındaki tek sayıları yazan kod.

baslangic=int(input("başlangıç: "))
bitis=int(input("bitiş: "))
i=baslangic

while i<bitis:
    if i%2==1:
        print(i)
    i+=1

#1-100 arasındaki sayıları yazdıran kod.

i=99
while i>1:
    print(i)
    i-=1

#Kullanıcıdan alınan 5 sayıyı bir listeye ekleyen kod.

numbers=[]
i=0
while i<5:
    sayi=int(input("Sayiyi giriniz: "))
    i+=1
    numbers.append(sayi)
numbers.sort()                  #Sayılar küçükten büyüğe sıralandı.
print(numbers)


#Kullanıcıdan alınan veriler ile dictionary türünde liste yapın.

urunler=[]
adet=int(input("Kaç adet ürün olacağını giriniz: "))
i=0
while (i<adet):
    name=input("Ürün adını giriniz: ")
    price=input("Ürün fiyatı giriniz: ")
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1
print(urunler)
for n in urunler:
    print(f"Ürünün adı: {n['name']} ve ürünün fiyatı: {n['price']}")