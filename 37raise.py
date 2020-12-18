#x=10
#if x>5:
#    raise Exception("X 5'den büyük değer alamaz.")
"""
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli Parola")

passoword="123456546aA"

try:
    check_password(passoword)
except Exception as ex:
    print(ex)
else:
    print("Parola Geçerli")
finally:
    print("Validation Tamamlandı.")
"""


class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name=name

try:
    p=Person("Aliiiiiiiiiiiiiiiiiii",1989)
except Exception as err:
    print(err)