# try:
#     file= open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası.")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file= open("newfile.txt","r",encoding="utf-8")

#       For döngüsü

# for i in file:
#     print(i,end="")

#       read() fonksiyonu
"""
Bu fonksiyonda imleç en sonda kalır. Dolayısıyla dosyayı kapatmadan
tekrar okuma yapılmak istendiğinde imleç sonda olduğu için okuma yapacak
yazı bulamaz.
"""

# content= file.read()
# print(content)

# content= file.read(6)   #% byte'lik yani 5 karakterlik okuma yapar. İmleç bittiği yerde kalır.
# print(content)


#       readline() fonksiyonu

# content= file.readline()        #Her seferinde tek bir satır okur.
# content= file.readline()
# print(content)


#       readlines() fonksiyonu

liste= file.readlines()     #Her satırı listenin bir elemanı olarak düzenler.
print(liste)

file.close()

