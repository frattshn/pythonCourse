myLis=[1,2,3]

class Movie:
    def __init__(self, title, director, duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Movie silindi.")

m=Movie("Filmin Adı", "Filmin Yönetmeni", 160)

print(str(myLis))
print(str(m))

print("+++++++++++++")

print(len(myLis))
print(len(m))

#del m

print(m)