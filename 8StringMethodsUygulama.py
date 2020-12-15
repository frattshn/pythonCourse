website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (44 saat)"


#1 " Helo World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result=" Hello World ".strip()
print(result)

#2 www.sadikturan.com içindeki sadikturan yazısı hariç her şeyi silin.
result="www.sadikturan.com".replace("www.","").replace(".com","")
print(result)

#3 course değişkeninin tüm harflerini küçük yapın.
course=course.lower()
print(course)

#4 website içindeki a harfi sayısını bulun.
result=result.count("a")
print(result)

#5 website www ile başlayıp com ile bitiyor mu?
#website=website.startswith("www")
#print(website)

#6 website içerisinde .com var mı?
website=website.find("com")
print(website)

