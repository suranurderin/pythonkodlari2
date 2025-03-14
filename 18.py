# Asagidaki ucgenin tepesinden baslayip asagidaki satirdaki bitisik 
# sayilara dogru ilerleyerek yukaridan asagiya maksimum toplam 23 olur.

 #     3
 #    7 4
 #   2 4 6
#   8 5 9 3

# Yani 3+7+4+9=23.

# Asagidaki ucgenin yukaridan asagiya maksimum toplamini bulun:

#                 75
#                95 64
#              17 47 82
#             18 35 87 10
#            20 04 82 47 65
#           19 01 23 75 03 34
#          88 02 77 73 07 63 67
#         99 65 04 28 06 16 70 92
#        41 41 26 56 83 40 80 70 33
#       41 48 72 33 47 32 37 16 94 29
#      53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
#  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOT: Sadece 16384 rota oldugundan her rotayi deneyerek bu sorunu 
# cozmek mumkundur. Ancak Problem 67, yuz satir iceren bir ucgenle 
# ayni zorluktur; kaba kuvvetle cozulemez, akilli bir yontem 
# gerektirir! ;O)

Liste = [
      [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# Problemi ucgenin en altindan yukariya coz
def maxtoplamibul(Liste):
    for row in range(len(Liste) -2, -1, -1): 
        for col in range(len(Liste[row])):
            # Hucrenin degerini, bir alt satirdaki iki komsu hucreden maksimum olani ekleyerek guncelleme
            Liste[row][col] += max(Liste[row +1][col], Liste[row + 1][col + 1])
    return Liste[0][0]

maxtoplam = maxtoplamibul(Liste)
print("Max toplam:", maxtoplam)