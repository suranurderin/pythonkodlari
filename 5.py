# 1'den 20'ye kadar olan tüm sayılara tam olarak bölünebilen en küçük pozitif sayı nedir?

num = 21 

while True: # en kucuk asal sayiyi bulana kadar devam eden dongu
    div = 2 # div (bolen) adli degiskeni 2 olarak baslatir.

    while num%div == 0 and div!=21: #num(sayi)'un div'e bolunebilir olup olmadigini kontrol eder. eger bolunebilirse ve div 21'den farkliysa, div'i 1 artirir ve dongu sonraki yinelemesine gecer. bu dongu num'un 21'den kucuk tum carpanlarini kontrol etmek icin kullanilir.  
        div+=1

    if div == 21: #  iç döngü tamamlandıktan sonra bolen'in 21'e eşit olup olmadığını kontrol eder. eger eşitse, sayi asal sayıdır.
        print(num) 
        break #donguyu sonlandirir

    num+=1 #num degiskenini 1 artirir ve dongunun sonraki yinelemesine gecer.