##
numbers=[]
for i in range(10):
    numbers.append(i)
print(numbers)

##
numbers=[x for x in range(10)]
print(numbers)

##
for x in range(10):
    print(x**2)
numbers=[x**2 for x in range(10)]
print(numbers)
##
numbers=[x*x for x in range(10) if x&3==0]
print(numbers)
##
myString="hello"
myList=[]

for letter in myString:
    myList.append(letter)
print(myList)

##
myList=[letter for letter in myString]
print(myList)
##
years=[1998,1987,1856,1993]
ages=[2019-x for x in years]  #2019-x listeye yazdırılacak olan değerdir.
print(ages)
##
results=[x if x%2==0 else "Tek" for x in range(1,10)]
print(results)

##
result=[]

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)
##
numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)
##
