# 600851475143 sayisinin en büyük asal çarpani nedir?

def findLargestPrimeFactor(n): # en buyuk asal carpan findLargestPrimeFactor fonksiyonu olarak tanimlanir. Bu fonksiyon n adli bir parametre alir.
  primeFactor = 1 # asal carpan yani primeFactor degiskeni 1 olarak baslatir.
  i = 2 #i degiskenini 2 olarak baslatir

  while i <= n / i: #i degiskeni n'nin karekokune esit veya kucuk oldugu surece # dongunun devam etmesini saglar. gereksiz kontrol islemlerini onler.
    if n % i == 0: # n'nin bolunebilir olup olmadigini kontrol eder, eger bolunebilirse i bir carpanidir.
      primeFactor = i # i' nin en buyuk asal carpan oldugunu varsayar ve primeFactor degiskenine atar
      n /= i # n'yi i'ye boler.
    else: #bolunebilir olmadigi durumda calisir
      i += 1 # degiskeni 1 arttirip dongunun sonraki yinelemesine gecer

  if primeFactor < n: primeFactor = int(n) # dongu tamamlandiktan sonra primeFactor degiskeninin n'den kucuk olup olmadigini kontrol eder. eger kucukse n kendisi en buyuk asal carpanidir.
  # primeFactor = int(n) n'in en buyuk asal carpan oldugunu belirler ve primeFactor degiskenine atar.

  return primeFactor # sonucu yani en buyuk asal carpani dondurur

print(findLargestPrimeFactor(600851475143)) # fonksiyonu 600851475143 sayisiyla cagirir ve sonucu ekrana yazdirir.