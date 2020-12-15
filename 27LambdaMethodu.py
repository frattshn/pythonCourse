#Map metodu ile listedeki elemanlara işlem yapma.
def square(num): return num**2
numbers=[1,3,5,7]
result=list(map(square, numbers))
print(result)

#Fonksiyon tanımlamadan Lambda Methodu ile aynı işlemi yapma.

numbers=[1,3,5,7]
for i in map(lambda num: num**2, numbers):
    print(i)



