import math
n = int(input("Dammi un numero intero: "))
sommaD = 0
if n >= 0:
    for i in range(1, 2 * n + 1, 2):
        print(i)
        sommaD = sommaD + i

radice_intera = math.isqrt(sommaD)
print(f"La somma è: {sommaD}, quadrato perfetto: {radice_intera** 2 == sommaD}")
    