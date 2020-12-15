ogrenciler={}

number=input("Öğrenci No'yu giriniz: ")
name=input("Öğrenci adı giriniz: ")
surname=input("Öğrenci soyadı giriniz: ")
phone=input("Telefon No giriniz: ")

"""
ogrenciler[number]={
    "Ad":name,
    "Soyad":surname,
    "Telefon":phone
}
"""
ogrenciler.update({
    number:{
        "Ad":name,
        "Soyad":surname,
        "Telefon":phone,
    }
})


print(ogrenciler)