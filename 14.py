#Pozitif tam sayilar kumesi icin asagidaki yinelemeli dizi tanimlanir:

#n -> n/2 (n cifttir)
#n -> 3n+1 (n tektir)

#Yukaridaki kurali kullanarak ve 13 ile baslayarak asagidaki diziyi olustururuz:

#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 ->2 ->1

#Bu dizinin (13'ten baslayip 1'de biten) 10 terim icerdigi görulmektedir. Henuz kanitlanamasa da (Collatz Problemi) tum baslangic ​​sayilarinin 1'de bittigi dusunulmektedir.  

#Bir milyonun altindaki hangi baslangic ​​numarasi en uzun zinciri olusturur?

#NOT: Zincir basladiktan sonra terimlerin bir milyonun uzerine cikmasina izin verilir.


## Collatz zincir uzunlugunu hesapla ve sonuclari memoize (tekrar hesaplama yapmamak icin hafizaya kaydetme) eder.
def collatz_chain_length(n, memo):
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 1
    
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    length = 1 + collatz_chain_length(next_n, memo)
    memo[n] = length
    return length

## Bir milyonun altindaki en uzun Collatz zincirini olusturan sayiyi bul
def longest_collatz_chain(limit):
    max_length = 0
    starting_number = 0
    memo = {}
    
    for i in range(1, limit):
        length = collatz_chain_length(i, memo)
        if length > max_length:
            max_length = length
            starting_number = i
    
    return starting_number, max_length

# Limiti bir milyon olarak belirleme 
limit = 1_000_000
number, chain_length = longest_collatz_chain(limit)
print(f"Bir milyonun altındaki en uzun Collatz zincirini başlatan sayı: {number}")
print(f"Bu zincirin uzunluğu: {chain_length}")
