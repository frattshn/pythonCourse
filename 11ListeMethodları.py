numbers=[5,7,9,11,5,10,95]
letters=["a","j","p","w","i","t"]

print(min(numbers))
print(min(letters))
print(max(numbers))
print(max(letters))

print(numbers[4:6])
print(letters[3:])

numbers[4]=40
print(numbers)

numbers.append(58)                          #Listenin en sonuna ekleme yapar.
print(numbers)
letters.append("r")
print(letters)

numbers.insert(1,10)                        #Yazılan index numarasından hemen önceki yere ekleme yapar.
print(numbers)
letters.insert(3,"m")
print(letters)

numbers.pop()                               #Verilen index numarasındaki elemanı siler.
print(numbers)
letters.pop(0)
print(letters)

numbers.remove(10)                          #Silmek istenilen karakteri siler.
print(numbers)

numbers.sort()                              #Listeyi büyükten küçüğe doğru sıralar.
print(numbers)
letters.sort()
print(letters)

numbers.reverse()                           #Listeyi tersine çevirir.
print(numbers)
letters.reverse()
print(letters)

print(numbers.count(10))                    #Numbers dizisi içinde kaç adet 10 olduğunu söyler.
print(letters.count("t"))

numbers.clear()                             #Listenin bütün elemanlarını siler.
print(numbers)
