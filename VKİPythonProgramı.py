kütle = float(input("Kütlenizi kilogram cinsinden giriniz... "))
boy = float(input("Boyunuzu metre cinsinden giriniz... "))
vki = kütle/(boy*boy)

if vki < 18.5:
    print(vki, " Zayıf")
elif vki >= 18.5 and vki <= 24.9:
    print(vki, " Sağlıklı")
elif vki >= 25 and vki <= 29.9:
    print(vki, " Şişman")
elif vki >= 30 and vki <= 39.9:
    print(vki, " Obez")
else:
    print(vki, " Aşırı(Morbid) Obez")