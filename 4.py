# İki üç basamaklı sayının çarpımından oluşan en büyük palindromu bulun.

def palindromMu(n): 
    return str(n) == str(n)[::-1] # n sayisinin palindrom olup olmadigini kontrol eder. str(n) ifadesi n sayisini bir dizeye donusturur. str(n)[::-1] ifadesi bu dizenin ters cevrilmis halini alir. Eger bu iki ifade esitse n sayisi palindromdur ve fonksiyon True degerini dondurur, aksi halde False degerini dondurur

mylist=[] # myList adinda bos liste olusturur. bu liste daha sonra bulunan palindrom carpimlari saklayacaktir.
for first_num in range(100,1000): # ilk sayi degiskenini 100 baslatip 999'a kadar artirarak bir ic dongu olusturur. Bu dongu uc basamakli tum ilk sayilari tarayacaktir.
    for second_num in range(100,1000): # bu da ikinci sayi icin 100'den 999'a kadar artirarak bir ic dongu olusturur. Bu ic dongu uc basamakli tum ikinci sayilari tarayacaktir.
        item = first_num*second_num # ilk sayi ve ikinci sayinin carpimini hesaplayip item degiskenine atar.
        if palindromMu(item): #item degiskeninin palindrom olup olmadigini kontrol eder.
            mylist.append(item) # eger palindromsa myList listesine ekler.
print(max(mylist)) #myList listesindeki en buyuk elemani ekrana yazdirir.