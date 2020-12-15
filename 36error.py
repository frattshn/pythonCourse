#error -> hata

#Error      python.org Built-in Exceptions
# print(a) => NameError
# int("12a") => ValueError
# print(10/0) => ZeroDivisionError
# print("denem"e) => SyntaxError




#error handling -> hata yönetimi

try:
    x= int(input("x: "))
    y= int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y için 0 girilemez")
except ValueError:
    print("x ve y için sayısal değer girmelisiniz.")
else:   #Except çalışmaz ise else kısmı çalışır.
    print("Her şey yolunda.")
#except (ValueError,ZeroDivisionError) as e:
#    print("Yanlış bilgi girdiniz.")
#    print(e) Hata tipini yazdırır.


while True:
    try:
        a= int(input("a: "))
        b= int(input("b: "))
        print(a/b)
    except Exception as error:
        print("Yanlış bilgi girdiniz. ",error)
    else:
        break
    finally:        #Her halükarda çalışır.
        print("Try Except sonlandı.")


