# n! n * (n-1) * ... anlamina gelir. * 3 * 2 * 1.
# ornegin, 10! = 10*9*...*3*2*1=3628800 ve 10! sayisindaki rakamlarin toplami 3+6+2+8+8+0+0=27'dir.
# 100! sayisindaki rakamlarin toplamini bulunuz.

import math #math modulundeki math.factorial() fonksiyonunu kullanacagız. 
#Bu fonksiyon bir tam sayinin faktoriyelini hesaplar.

# Faktoriyel hesaplama 
n = 100
factorial_result = math.factorial(n)

# Rakamlari ayirip string degere donusturme ve rakamlari toplama
digit_sum = sum(int(digit) for digit in str(factorial_result))

# Sonucu yazdirma
print(digit_sum)
