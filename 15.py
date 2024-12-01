#2 x 2'lik bir izgaranin sol ust kosesinden baslayip yalnizca saga ve asagi dogru hareket edebilen, 
# tam olarak sag alt koseye giden yollar vardir.

#20 x 20'lik bir izgarada bu sekilde kac tane rota vardir?

from math import comb

# Kombinasyon hesaplamasi: C(40, 20)
def grid_paths(grid_size):
    total_moves = 2 * grid_size  # Sag ve asagi hareket toplami
    return comb(total_moves, grid_size)

# 20x20 izgaranin yollari
grid_size = 20
paths = grid_paths(grid_size)
print(f"20x20 izgarada toplam yollar: {paths}")