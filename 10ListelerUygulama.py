markalar=["BMW","Mercedes","Opel","Mazda"]

#Liste kaç elemanlıdır?
print(len(markalar))

#Listenin ilk ve son elemanı nedir?
print(markalar[0],markalar[3])

#Mazda ismini Toyota ile değiştirin.
markalar[-1]="Toyota"
print(markalar)

#Mercedes listenin bir elemanı mıdır?
sonuc="Mercedes" in markalar                                #Mercedes markalar dizisinde midir sorusu soruldu
print(sonuc)

#Listenin ilk üç elemanını yazdırın
print(markalar[0:3])

#Listenin son iki elemanı yerine Toyota ve Renault yazdırın
markalar[-2:]=["Toyota","Renault"]
print(markalar)

#Listeye Audi ve Nissan değerlerini ekleyin
markalar=markalar +["Audi","Nissan"]
print(markalar)

#Listenin son elemanını silin
del markalar[-1]
sonuc=markalar
print(sonuc)

#Liste elemanlarını tersten yazdırın
sonuc=markalar[::-1]
print(sonuc)

#studentA= Fırat, Şahin, 2000, [98,100,95]
studentA=["Fırat","Şahin",2000,[95,100,95]]
print(studentA[0])
print(studentA[3])

sonuc=f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}'dir.'"
print(sonuc)