names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

#"Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

#"Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)

#"Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)

#"Yağmur" isminin indexini bulunuz.
index=names.index("Yağmur")
print(index)

#"Ali" listenin bir elemanı mıdır?
sonuc="Ali" in names
print(sonuc)

#Liste elemanlarını ters çevirin.
names.reverse()
print(names)

#Liste elemanlarını alfabetik olarak sıralayın.
names.sort()
print(names)

#str="Chevrolet,Dacia" yı liste haline çevirin
str="Chevrolet,Dacia"
result=str.split(",")
print(result)

#years dizisinin en büyük ve en küçük elemanını yazdırın.
min=min(years)
max=max(years)
print(min)
print(max)

#years dizisi içinde kaç tane 1998 değeri vardır?
result=years.count(1998)
print(result)

#years dizisin tüm elemanlarını siliniz.
years.clear()
print(years)

#Kullanıcıdan alacağınız 3 adet marka bilgisini bir listede saklayınız.
markalar=[]

marka=input("Marka ismi giriniz: ")
markalar.append(marka)

marka=input("Marka ismi giriniz: ")
markalar.append(marka)

marka=input("Marka ismi giriniz: ")
markalar.append(marka)

print(markalar)