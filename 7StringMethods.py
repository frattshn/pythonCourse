message=" Hello niggas, my name is Fırat."

message=message.upper()             #Bütün harfleri büyütür.
print(message)                      

message=message.lower()             #Bütün harfleri küçültür.
print(message)

message=message.title()             #Her kelimenin ilk harfini büyük yazar.
print(message)

message=message.capitalize()        #Cümlenin yalnızca ilk harfini büyük yazar.
print(message)

message=message.strip()             #Cümlenin başındaki boşluk karakterini silerek yazar.
print(message)

message=message.split()             #Cümleyi dizi haline getirir.
print(message)
#print(message[1])

#message=message.split(".")         #Cümleyi . sembolüne göre ayırır.
#print(message)

message=" ".join(message)           #Bölünmüş cümleyi arada boşluk bırakarak birleştirir.
print(message)

index= message.find("niggas")       #Message değişkeninde niggas kelimesinin olup olmadığını söyler. Var ise ilk harfinin numarasını yazdırır.
print(index)

isTrue= message.startswith("h")     #Message cümlesi h harfi ile mi başlar? sorusu sorulur. Büyük küçük harf duyarlılığı vardır..
print(isTrue)

isTrue2= message.endswith("t")      #Message cümlesi t harfi ile mi biter? sorusu sorulur. Büyük küçük harf duyarlılığı vardır.
print(isTrue2)

#message=message.replace(" ","+").replace("a","y")   #Cümle içerisindeki kelimeleri değiştirir.
#print (message)

message=message.center(50,"*")      #Cümleyi toplam 50 karakter olacak şekilde düzenler ve ortalar. İkinci bölümdeki yazılan boşluklara gelir.
print(message)

