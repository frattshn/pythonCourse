# # FONKSİYONLARA ÖZELLİK EKLEMEK İÇİN KULLANILIR

# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello "+name)


# def sayGreeting():
#     print("greeting")


# #sayHello= my_decorator(sayHello)
# sayGreeting= my_decorator(sayGreeting)

# sayHello("Fırat")
# #sayGreeting()



import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start= time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish= time.time()
        print("Fonksiyon "+func.__name__+ str(finish-start)+" saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(a):
    print(math.factorial(a))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(5)
toplama(50,8)








