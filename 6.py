# Bu nedenle ilk on doğal sayının karelerinin toplamı ile toplamın karesi arasındaki fark 3025-385=2640'tır.

# İlk yüz doğal sayının karelerinin toplamı ile toplamın karesi arasındaki farkı bulun.

def farki_bul():

  # İlk 100 doğal sayının karelerinin toplamı
  kareler_toplami = 0
  toplamlar = 0
  for i in range(1, 101):
    kareler_toplami += i**2
    toplamlar += i

  # İlk 100 doğal sayının toplamının karesi
  toplam_karesi = toplamlar**2

  # Farkı bulma
  fark = toplam_karesi - kareler_toplami

  return fark

sonuc = farki_bul()
print("Fark:", sonuc)