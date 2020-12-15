#Range içine tek bir sayı yazdırılırsa 0dan başlayarak içine yazılan yazı kadar sayı basar.
for item in range(10):
    print(item)


#2'den başlayıp 80'e kadar 3er arttırarak yazdıran kod.
for i in range(2,80,3):
    print(i)


greeting="hello there"
index=0

#Enumerate komutu olmadan aşağıdakini yapma.
for letter in greeting:
    print(f"index: {index} letter: {letter}")
    index+=1


#Enumerate komutu index,value şeklinde yazdırır.
greeting="hello"

for i in enumerate(greeting):
    print(i)


#Zip komutu birebir olan  indexleri birleştirir.

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for i in zip(list1,list2,list3):
    print(i)