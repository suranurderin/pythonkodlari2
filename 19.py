# 1 ocak 1900 pazartesiydi.

# Eylul, nisan, haziran ve kasim aylarinda otuz gun var,
# Geri kalan aylarda otuz bir gun var,
# Yagmur camur demeden sadece subatta 28 gun diger yillarda 29 gun var.

# Artik yil, 4'e esit olarak bolunebilen herhangi bir yilda olusur, 
# ancak 400'e bolunemeyen bir yuzyilda olmaz.

# Yirminci yuzyil boyunca (1 Ocak 1901 - 31 Aralik 2000) kac Pazar gunu ayin ilk gunune denk gelmistir?

# Yil kontrolu
def isleapyear(year):
    ##Bir yilin artik yil olup olmadigini kontrol etme
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Pazar gunlerini sayma
def countsundaysonfirst(startyear, endyear):
    ##Belirtilen yillar arasinda (startyear ve endyear dahil) ayin ilk gunu Pazar olan gunlerin sayisini dondurur.
    
    # Aylarin gun sayilari
    daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1 Ocak 1900 Pazartesi (0: Pazartesi, 6: Pazar)
    dayofweek = 0  # İlk gun Pazartesi (1 Ocak 1900)
    sundaycount = 0

    # 1 Ocak 1901'in gununu bulmak icin 1900 yilini ekliyoruz
    for year in range(1900, startyear):
        dayofweek += 366 if isleapyear(year) else 365
    dayofweek %= 7  # 1 Ocak 1901'in haftanin hangi gunu oldugunu bulduk

    # Belirtilen aralikta dongu
    for year in range(startyear, endyear + 1):
        for month in range(12):
            # Eger gun Pazar ise sayaci arttir
            if dayofweek == 6:
                sundaycount += 1
            # O ayin gun sayisi kadar ileri git
            dayofweek += daysinmonth[month]
            # Eger subat ise ve yil artik yilsa 1 gun daha ekle
            if month == 1 and isleapyear(year):  # subat ve artik yil kontrolu
                dayofweek += 1
            dayofweek %= 7  # Haftanin gununu belirlemek icin mod al

    return sundaycount

# 1 Ocak 1901 - 31 Aralik 2000 araliginda Pazar gunleri sayimi
sundaysonfirst = countsundaysonfirst(1901, 2000)
print(sundaysonfirst)