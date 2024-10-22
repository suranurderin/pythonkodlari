# a+b+c=1000 olan tam olarak bir Pisagor üçlüsü vardır. Python'da abc çarpımını bulun.

# 1000'e esit uc sayiya ihtiyacimiz oldugundan, zamandan tasarruf etmek icin;
# 400'e kadar yineleme yapiyoruz. Bunun nedeni a ve b'nin 400'den daha az 
# degerli olacagini bilmemizdir cunku a < b < c

for a in range (1,400):
    for b in range (1, 400):

        # 1000'den a ve b'yi cikararak c'yi bul c icin donguye gerek yok
        c = (1000-a)-b

        #her sayi bir sonrakinden kucuk olmali
        if a < b < c:

            #sayilarin pisagor baglantisi olup olmadigini kontrol et
            if a**2 + b**2 == c**2:
                print(a*b*c)
