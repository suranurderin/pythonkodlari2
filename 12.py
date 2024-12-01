# ucgen sayi dizisi, doğal sayilarin eklenmesiyle olusturulur. 
# Yani 7. ucgen sayisi 1+2+3+4+5+6+7=28 olacaktir. İlk on terim soyle olacaktir:
# 1,3,6,10,15,21,28,36,45,55,...

# İlk yedi ucgen sayisinin carpanlarini siralayalim:
# 1: 1
# 3: 1 3
# 6: 1 2 3 6
# 10: 1 2 5 10
# 15: 1 3 5 15
# 21: 1 3 7 21
# 28: 1 2 4 7 14 28

# 28'in besten fazla boleni olan ilk ucgen sayisi olduğunu gorebiliriz.

# Bes yuzun uzerinde boleni olan ilk ucgen sayisinin değeri nedir?

##ucgen sayisini hesaplayan formul:
## Tn = (n*(n+1))/2

def bolensayisi(n):
    ##Bir sayinin bolenlerinin sayisini hesaplama
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def ucgensayisi(minbolen):
    ##Belirli bir bolen sayisindan fazla boleni olan ilk ucgen sayisini bulma
    n = 1
    while True:
        # n'inci ucgen sayisini hesapla
        ucgen_no = n * (n + 1) // 2
        # Bolenlerin sayisini bul
        if bolensayisi(ucgen_no) > minbolen:
            return ucgen_no
        n += 1

## 500'den fazla boleni olan ilk ucgen sayisini bulma
result = ucgensayisi(500)
print("500'den fazla boleni olan ilk ucgen sayisi:", result)
