x,y,z=2,5,10
numbers=1,5,7,10,6

#Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
ilksayi=int(input("İlk sayıyı giriniz: "))
ikincisayi=int(input("İkinci sayıyı giriniz: "))
print((ilksayi*ikincisayi)-(x+y+z))

#y'nin x'e kalansız bölümünü hesaplayınız.
print(y//x)

#x,y,z toplamının mod 3'ünü hesaplayınız.
print((x+y+z)%3)

#y'nin x'inci kuvvetiniz hesaplayınız.
print(y**x)

#x,*y,z=numbers işlemine göre z'nin küpü kaçtır.
x,*y,z=numbers
print(z**3)

#x,*y,z=numbers işlemine göre y değerleri toplamı kaçtır?
print(y[0]+y[1]+y[2])