maasAli=5000
maasAhmet=4000
vergi=0.27
print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

#Değişken Tanımlama Kuralları
#Değişken ismi rakam ile başlayamaz.
#İçine değer atamadan değişken tanımlanamaz.

sayi1=10
print(sayi1)

sayi1=20
print(sayi1)

sayi1+=30 #Sayi1 değişkenine 30 eklendi
print(sayi1)

#Değişken isimlerinde büyük küçük harf duyarı vardır.

x=1                     #integer
y=2.5                   #float
name= "Fırat"           #string
isStudent= True         #bool

firstName="Fırat"
lastName=" Şahin"
print(firstName+lastName)  #Fırat Şahin


degisken1,degisken2,degisken3= (1, 5.6, "Yiğido")  #Tek satırda değişken tanımlama.


"""
paragraf
halinde
yorum
satırı
"""

musteriAdi="Ali"
musterisoyAdi="Koç"
musteriAdSoyad= musteriAdi+" "+musterisoyAdi
print(musteriAdSoyad)