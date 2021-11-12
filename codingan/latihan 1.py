print(" Program Menampilkan n bilangan acak yang lebih kecil dari 0.5")
print(" ---------------------------------------------------------------")
print()

from random import random
n=int(input("Masukan Nilai N : "))
for i in range(n):
    while 1:
        n=random()
        if n < 0.5:
            break
    print("data ke: ",i,"=>",n)

print("Selesai")
