"""
1-100 arasonda rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın
Kullanıcının 5 hakkı olsun 100 üzerinden puanlama yapın. Her soru 20 puan.
Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

import random

sayi=random.randint(1,10)
can=int(input("Kaç hakkınız olsun?"))
hak=can
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("Tahmininizi giriniz: "))

    if sayi==tahmin:
        print(f"Tebrikler {sayac}.defada bildiniz. Puanınız: {100-(100/can*(sayac-1))}")
        break
    elif sayi>tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak==0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")