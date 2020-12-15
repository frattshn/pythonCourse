#Çift sayıların toplamını yazdıran kod.
#Continue komutuna gelince program orayı atlar ve başa döner.


toplam=0
i=0
while i<100:
    i+=1
    if i%2==1:              #Tek sayılar gelince atlıyor.
        continue
    toplam+=i
print(toplam)




#MemduhFırat isminde u harfine gelince atladı fakat çalışmaya devam etti.


isim="MemduhFırat"
for i in isim:
    if i=="u":
        continue
    print(i)


#Break komutuna gelene kadar sayıları yazdırır. Fakat break komutuna gelince kod çalışmayı durdurur.
a=0
while a<58:
    if a==27:
        break
    print(a)
    a+=1
