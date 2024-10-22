# İki milyondan küçük asal sayıların toplamını bulunuz.

#num asal ise True degilse False

#Mantik;
# num 1'den kucuk veya ona esitse, asal degildir
# num 3'ten kucuk veya ona esitse asaldir
# num 2 veya 3"e bolunebiliyorsa asal degildir
# kalan durumlar icin bolunebilirligi 5'ten baslayarak 4'er artirarak kontrol edilir (tek sayilar icin)
# num belirtilen araliktaki herhangi bir i veya i+2'ye bolunebiliyorsa asal degildir
# bolen bulunamazsa num asaldir

def isprime(num):
    if num <= 1: 
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False 
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 4
    return True

def sum_primes_below(limit): #asal sayilar icin ust sinir
    sum_of_primes = 0 
    for num in range(2, limit): # sinirin altindaki tum asal sayilarin toplamini dondurur.
        if isprime(num): # her sayi icin asal olup olmadigini kontrol eder
            sum_of_primes += num # sayi asal ise sum_of_primes'a ekler
    return sum_of_primes 

sum_of_primes = sum_primes_below(2000000)
print('2 milyondan kucuk asal sayilarin toplami', sum_of_primes)
