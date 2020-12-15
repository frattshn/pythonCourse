"""
list=[1,"iki",3]
list[0]=2
print(list[0])

tuple=(1,"iki",3)               Listelerde daha sonradan atama yapılabilir fakat tuplede atama yapılamaz.
tuple[0]=2
"""

"""
sehirler=["kocaeli","istanbul"]
plakalar=[41,34]
print(plakalar[sehirler.index("kocaeli")])
"""

plakalar={"kocaeli":41, "istanbul":34}
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"]=6
print(plakalar)

users={
    "firatsahin":{
        "age":36,
        "roles":["user"],
        "email":"frtshn907@gmail.com",
        "adress":"sivas",
        "phone":5374912202
    },
    "memduhfirat":{
        "age":58,
        "roles":["admin","user"]
    }
}

print(users["firatsahin"]["email"])
print(users["firatsahin"]["age"])
print(users["firatsahin"]["adress"])

print(users["firatsahin"]["roles"][0])
print(users["memduhfirat"])