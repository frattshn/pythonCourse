# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erisme_kodu)
# dosya_erisme_kodu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (write) Yazma modu. Dosyayı konumda oluşturur. Eski bilginin üzerine yazar.
# "a": (Append) Ekleme modu. Dosya konumda yoksa oluşturur. Eski bilgiler silinmez, ekleme yapılır.
# "x": (Create) Oluşturma modu. Dosya zaten varsa hata verir.
# "r": (Read) Okuma modu. Varsayılan. Dosya konumda yoksa hata verir.

#file= open("C:/Users/Public/newfile.txt","w")
#print(file)

#file= open("new_file.txt","w", encoding="UTF-8")
#file.write("Memduh Fırat Şahin")
#file.close()

#file= open("newfile.txt", "a", encoding="utf-8")
#file.write("Fırat Şahin\n")
#file.close()

file= open("newfile2.txt", "x", encoding="utf-8")

