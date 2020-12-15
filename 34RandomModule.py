import random

result= random.random() #0.0-1.0
result= random.random()*100
result= int(random.uniform(10,100))
result= random.randint(1,100)

greeting= "Hello There"
names=["Ali", "Yağmur","Deniz","Cenk","Ahmet","Efe"]

#result=names[random.randint(0, len(names)-1)]

result= random.choice(names)
result= random.choice(greeting)

liste=list(range(10))   #0'dan 9'a kadar sayılardan oluşan liste oluşturuldu.
random.shuffle(liste)
result=liste

liste=range(100)
result= random.sample(liste,3)
result= random.sample(names,2)

print(result)