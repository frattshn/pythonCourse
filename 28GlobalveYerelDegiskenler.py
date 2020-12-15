
x=50
def test(x):
    print(f"x: {x}")

    x=100
    print(f"changed x to {x}")
test(x)     #Burada yerel olan x ile işlem yapılıyor.
print(x)    #Burada global x ile işlem yapılıyor.

#################

a=25
def test2():
    global a    #a'nın tanımı global olarak değiştirildi.
    print(f"a: {a}")

    a=50
    print(f"changed a to {a}")
test2()
print(a)

