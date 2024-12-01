# 1'den 5'e kadar olan sayilar one, two, three, four, five seklinde yaziyla yazilirsa toplamda 3+3+5+4+4=19 harf kullanilir.
# 1'den 1000 (one thousand) dahil tum sayilar yaziyla yazilsaydi kac harf kullanilirdi?
# NOT: Bosluklari veya kisa cizgileri saymayin. ornegin 342 (three hundred and forty-two) sayisinda 23 harf, 
# 115 (one hundred and fifteen) sayisinda ise 20 harf bulunmaktadir. Sayilari yazarken "ve" kullanimi İngiliz 
# kullanimina uygundur.

#İngilizce sayilara gore cozumu yapilmistir.

# Sayilari yuzler, onlar ve birler basamagına ayırma
def number_to_words(n):
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Sayiyi yaziya cevirme
    if 1 <= n <= 9:
        return ones[n-1]
    elif 10 <= n <= 19:
        return teens[n-10]
    elif 20 <= n <= 99:
        return tens[n//10 - 2] + (ones[n%10 - 1] if n%10 != 0 else "")
    elif 100 <= n <= 999:
        return ones[n//100 - 1] + "hundred" + ("and" + number_to_words(n%100) if n%100 != 0 else "")
    elif n == 1000:
        return "onethousand"

# Her sayiyi yaziya cevirme ve harf uzunlugunu bulma
def letter_count_up_to(limit):
    total = 0
    for i in range(1, limit + 1):
        total += len(number_to_words(i))
    return total

# 1'den 1000'e kadar toplam harf sayisi:
print(letter_count_up_to(1000))

