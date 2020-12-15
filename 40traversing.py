"""
With ile yazılırsa bloktan sonra otomatik olarak dosya kapanır.
"""

with open("newfile2.txt","r",encoding="utf-8") as file:
    content= file.read(10)  #İlk 10 karakteri okudu.
    print(content)
    file.seek(5)        #İmleci 5. konuma gönderdi.
    print(file.tell())  #İmlecin hangi konumda olduğunu söyler.