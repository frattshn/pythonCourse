#Girilen 2 sayıdan hangisi büyüktür?

"""
a=int(input("a değerini giriniz "))
b=int(input("b değerini giriniz "))

result= (a<b)
print(f"a değeri: {a} b değerinden: {b} küçük müdür? {result}")

#Kullanıcıdan 2 adet vize (%60) ve 1 final (%40) notu al. Ortalama 50ye eşit veya büyükse geçti,
#değilse kaldı yazsın.

vize1=float(input("1.Vize: "))
vize2=float(input("2.Vize: "))
final=float(input("Final: "))

ortalama= ((vize1+vize2)/2)*6/10 + final*4/10
result= (ortalama>=50)
print(f"Not Ortalamanız: {ortalama} \nDersten geçtiniz mi? {result}")

#Girilen sayının tek mi çift mi olduğunu yazdırın.

x=int(input("Sayıyı giriniz: "))
tekcift= (x%2==0)
print(f"Girilen sayı: {x}.\nSayı çift mi? {tekcift}")

#Girilen sayı negatif mi pozitif mi?

y=float(input("Sayıyı giriniz: "))
pozitifmi= (y>0)
print(f"Girilen sayı: {y}.\nSayı pozitif mi? {pozitifmi}")
"""

#Parola ve email bilgisini isteyip doğruluğunu kontrol edin.
email, parola="email@firatsahin.com","parola123"
emailx=str(input("Email giriniz: "))
parolax=str(input("Parola giriniz: "))
esitmi= (email==emailx.lower().strip()) and (parola==parolax.lower().strip())

print(f"Girdiğiniz bilgiler uyuştu mu? {esitmi}")