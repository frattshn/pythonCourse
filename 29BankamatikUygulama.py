#miktar=input("Çekmek istediğiniz tutarı giriniz: ")

FiratHesap={
    "Ad": "Memduh Fırat Şahin",
    "HesapNo": "12354648",
    "Bakiye": 3000,
    "EkHesap": 2000
}

ZahirHesap={
    "Ad":"Zahir Şahin",
    "HesapNo":"1236465",
    "Bakiye":2000,
    "EkHesap":1000
}

def ParaCek(hesap, miktar):
    print(f"Merhaba {hesap['Ad']}")

    if (hesap["Bakiye"]>=miktar):
        hesap["Bakiye"]-=miktar

        print("Paranızı Alabilirsiniz.")
    else:
        toplam= hesap["Bakiye"]+ hesap["EkHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi= input("Ek Hesap Kullanılsın Mı? e/h")
            
            if ekHesapKullanimi =='e':
                ekHesapKullanilacakMiktar=miktar-hesap["Bakiye"]
                hesap["Bakiye"]=0
                hesap["EkHesap"]-=ekHesapKullanilacakMiktar

                print("Paranızı Alabilirsiniz.")
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} lira bulunmaktadır.")
        else:
            print("Yetersiz Bakiye.")

def bakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['EkHesap']} TL'dir.")


ParaCek(FiratHesap, 2000)
bakiyeSorgula(FiratHesap)

print("**********************")
ParaCek(FiratHesap, 2000)
bakiyeSorgula(FiratHesap)






