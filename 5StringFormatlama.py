name="Fırat"

surname="Şahin"

age="20"

print("My name is {} {} and I am {} years old.".format(name, surname, age))

print("My name is {1} {0} and I am {2} years old.".format(name, surname , age))

print("My name is {n} {s} and I am {a} years old.".format(n=name, s=surname, a=age))

print(f"My name is {name} {surname} and I am {age} years old.")

result = 2/7

print("The result is {r:1.4}.".format(r=result))   #İlk rakam boşluk sayısını ifade eder. İkinci rakam ise noktadan sonra kaç basamak alınacağını gösterir.

print("The result is {r:1.2}.".format(r=result))   #İlk rakam boşluk sayısını ifade eder. İkinci rakam ise noktadan sonra kaç basamak alınacağını gösterir.
