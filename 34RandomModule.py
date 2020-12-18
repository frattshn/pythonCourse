import random

result= random.random() #0.0-1.0
print(result)
result= random.random()*100
print(result)
result= int(random.uniform(10,100))
print(result)
result= random.randint(1,100)
print(result)

greeting= "Hello There"
names=["Ali", "Yağmur","Deniz","Cenk","Ahmet","Efe"]

#result=names[random.randint(0, len(names)-1)]

result= random.choice(names)
print(result)

result= random.choice(greeting)
print(result)

liste=list(range(10))   #0'dan 9'a kadar sayılardan oluşan liste oluşturuldu.
print(liste)
random.shuffle(liste)
result=liste
print(result)

liste=range(100)
result= random.sample(liste,3)
print(result)
result= random.sample(names,2)
print(result)