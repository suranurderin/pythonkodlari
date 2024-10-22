# Fibonacci dizisindeki değerleri dört milyonu aşmayan terimleri ele 
# alarak, çift değerli terimlerin toplamını bulunuz.

total = 0 # total degiskeni 0 ile baslatir.
x, y = 0, 1 # x ve y degiskenleri sirasiyla 0 ve 1 olarak baslatir. 
# Bu degiskenler, Fibonacci dizisinin ardisik iki terimini temsil eder.

while y < 4000000: # y degiskeni 4000000'dan kucuk oldugu surece dongunun 
# devam etmesini saglar
    x, y = y, x + y # Fibonacci dizisinin yeni terimini hesaplar, x ve y 
    # degiskenlerinin degerleri degistirilir, x'in eski degeri y'ye atanir 
    # # ve y'nin eski degeri x ile y'nin toplamina atanir.
    if x % 2: # x degiskeninin mod 2'ye gore kalaninin 0 olup olmadigini
    # kontrol eder. eger kalan 0 degilse, yani x tek sayiysa, continue 
    # ifadesi dongunun sonraki yinelemesine gecer.
        continue
    total += x # x degiskeni cift sayiysa total degiskenine eklenir. 

print (total) 
