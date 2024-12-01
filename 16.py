# 2^15 = 32768 ve rakamlarinin toplami 3+2+7+6+8=26'dir.

# 2^1000 sayisinin rakamlarinin toplami kactir?

# 2^1000 sayisini hesaplama
x = 2**1000

# Cikan sonuctaki degerleri ayirma
x = str(x)

# Sonucu ayirma
digits = [int(char) for char in x]

# Ilk 10 rakam (kontrol amacli)
print("İlk 10 rakam:", digits[:10])

# Toplam rakam sayisini bulalim
print("Toplam rakam sayısı:", len(digits))

# Sonuc 302, bu 302 rakami toplayalim
toplam = sum(digits)
print(toplam)