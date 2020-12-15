#Inheritance (Kalıtım): Miras alma

#Person => name, lastname, age, eat(), drink()
#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)


class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
        print("Person Created.")

    def who_am_i(self):
        print("I am a Person.")

    def eat(self):
        print("I am eating.")

class Student(Person):  #Person İçeriğini Kopyaladı
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname ,lname)   #Person class'ının da çalışmasını sağladı.
        self.studentNumber= number
        print("Student Created.")
    
    #override olur yani temeli ezer
    def who_am_i(self):
        print("I am a Student.")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch=branch
        
    def who_am_i(self):
        print(f"I am a {self.branch} Teacher.")

p1= Person("Fırat", "Şahin")
s1=Student("Memduh", "Fırat", 525)
t1=Teacher("Serkan", "Yılmaz", "Math")

print(p1.firstname+ " "+ p1.lastname)
print(s1.firstname+ " "+ s1.lastname+" "+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
