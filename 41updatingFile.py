# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("Ekleme Yapıldı ")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

"""
        Sayfa sonunda güncelleme yapma.
a metodu ile (append) sona ekleme yapılır.
"""
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nSivasspor")

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

"""
        Sayfa başında güncelleme yapma.
"""

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content= file.read()
#     content= "Sivasspor\n"+ content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#          print(file.read())


"""
        Sayfa ortasında güncelleme yapma.
"""

with open("newfile.txt","r+",encoding="utf-8") as file:
        list= file.readlines()
        list.insert(1,"Rıza Çalımbay\n")
        file.seek(0)
        for i in list:
                file.write(i)

with open("newfile.txt","r",encoding="utf-8") as file:
        print(file.read())