#class
class Person:

    #class attributes
    address="No information."

    #constructor (yapıcı metod)
    def __init__(self, name, year):
        
        #object attributes
        self.name=name
        self.year=year
        print("init metodu çalıştı.")

    #instance methods
    def intro(self):
        print("Hello There I am "+self.name)

    def calculateAge(self):
        return 2020- self.year



#object (instance)
p1=Person(name="Memduh", year=2000)     #Yalnızca değerler de girilebilirdi.
p2=Person(name="Fırat", year=1998)

#updating
p1.name="Şahin"
p1.address="Sivas"


#accessing object attributes
print(f"p1: name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2: name: {p2.name} year: {p2.year} address: {p2.address}")

p1.intro()
p2.intro()

print(f"Adım: {p1.name} ve yaşım: {p1.calculateAge()}")

print(p1)
print(p2)



#Daire Class'ı oluşturuldu
class Circle:
    #Global bir değişken oluşturuldu.
    pi=3.14

    def __init__(self, yaricap=1): #Yarıçapa değer girilemez ise 1 olarak alır.
        self.yaricap=yaricap

    def cevreHesapla(self):
        return 2*self.pi*self.yaricap

    def alanHesapla(self):
        return self.pi*(self.yaricap**2)
c1=Circle()
c2=Circle(5)

print(f"C1'in çevresi: {c1.cevreHesapla()}, alanı: {c1.alanHesapla()}")
print(f"C2'nin çevresi: {c2.cevreHesapla()}, alanı: {c2.alanHesapla()}")