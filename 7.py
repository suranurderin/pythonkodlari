# 10001. asal sayı kaçtır?

def asal(n):
    if n < 2: return
    # Bir sayının çarpanları genellikle eş çiftler halindedir. Örneğin, 36'nın çarpanları 2 ve 18, 3 ve 12 gibi eş çiftlerdir. Bu nedenle, bir sayının bir çarpanı karekökünden büyükse, diğer çarpanı kesinlikle karekökünden küçüktür. Dolayısıyla, bir sayının bütün çarpanlarını kontrol etmek için sadece kareköküne kadar olan sayıları kontrol etmemiz yeterlidir. Bu yuzden;
    for i in range(2, int(n**0.5) + 1): # dongu i degiskenini 2'den baslayarak n sayisinin karekokunun tam sayi kismina kadar artirarak tekrarlar.
        if n % i == 0: # dongunun her adiminda n sayisi i ile bolunuyor mu diye kontrol edilir. 
            return False
    return True

# n'inci asal sayiyi dondurme
def nthAsal(n):
    asalSayilarinSayisi = 0 # degiskene 0 degerini atar. bu degisken su ana kadar kac tane asal sayi bulundugunu takip etmek icin kullanilir.
    prime = 1 # 1 degeri tanimlanir. bu degisken asal olup olmadigi kontrol edilecek sayiyi temsil eder.

    while asalSayilarinSayisi < n: # dongu asalSayilarinSayisi degiskeni n degerinden kucuk oldugu surece devam eder.
        prime += 1
        if asal(prime): # prime degiskeninin degerinin asal olup olmadigini kontrol eder. eger prime asal bir sayiysa bu kosul devam eder ve asalSayilarinSayisi degiskeni 1 arttirilir.
            asalSayilarinSayisi += 1
    return prime # dongu tamamlandiginda, en son bulunan asal sayinin degerini dondurur. 

print(nthAsal(10001))
