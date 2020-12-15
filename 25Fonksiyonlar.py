def toplam(a,b,c):
    return sum((a,b,c))
sonuc=toplam(10,20,30)
print(sonuc)

print("#####################################")

def toplam(*parametreler):                  # *parametreler demek istediği kadar değer alabilir anlamına gelir.
    return sum((parametreler))              # sum içine gönderilen değerleri toplar.
sonuc=toplam(10,25,94,846,9846,1,12)
sonuc2=toplam(20,50,44,58)
print(sonuc)
print(sonuc2)

print("#####################################")

