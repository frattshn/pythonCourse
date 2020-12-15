def usalma(number):

    def inner(power):
        return number**power
    return inner


two=usalma(2)
three=usalma(3)

print(two(3))
print(three(5))


def yetki_sorgula(page):
    def inner(role):
        if role=="Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(page, role)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(page, role)
    return inner

user1=yetki_sorgula("Product Edit")
print(user1("Admin"))

user2=yetki_sorgula("Software Engineering")
print(user2("Junior Admin"))



def islem(islem_adi):

    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi=="Toplama":
        return toplama
    
    if islem_adi=="Carpma":
        return carpma
    
toplama_islemi=islem("Toplama")
print(toplama_islemi(1,3,5,7,9))

carpma_islemi=islem("Carpma")
print(carpma_islemi(1,5,2,6))