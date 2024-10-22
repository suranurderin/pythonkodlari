# 1000'in altindaki 3 veya 5'in tum katlarinin toplamini bulun.

toplam = 0 # baslangic degeri 0 olarak atanir
for i in range(1,1000): # 1  ile 999 arasindaki tum degerleri i degiskeni ile dolasiyor
    if i % 3 == 0 or i % 5 == 0: # bu kosul ifadesi her i degeri icin kontrol yapar.
        # eger i sayisi 3'e veya 5'e tam bolunebiliyorsa (i % 3 == 0 ya da i % 5 == 0), kosul dogru olur.
        # % operatoru, mod alma islemi yapar; yani bir sayinin bir baska sayiya bolumunden kalanini bulur.
        # eger kalan 0 ise, sayi tam bolunebiliyordur.

        toplam += i # eger sayi 3'e veya 5'e tam bolunuyorsa o sayi toplam degiskenine eklenir. bu islem, toplam = toplam + i demektir.

print(toplam) # en son degeri (yani 1 ile 999 arasindaki 3 veya 5'e bolunebilen sayilarin toplami) ekrana yazdirilir
