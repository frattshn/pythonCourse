#Value Tipleri--> String ve Number
#Bu veri tiplerinde verinin kendisiyle ilgilenilir.

x=5
y=20
x=y
y=15
print(x,y)


#Reference Tipleri--> List
#Bu veri tiplerinde verinin adresiyle ilgilenilir.
#Yapılan değişiklikler her iki listede de geçerli olur.

a=["muz","armut","elma"]
b=["muz","armut","elma"]
a=b
b[0]="erik"
print(a,b)