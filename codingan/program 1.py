print(" Menghitung Total Keuntungan")
print(" ---------------------------")
print()

modal=1000000000
laba=[modal*0, modal*0, modal*1/100, modal*1/100, modal*5/100, modal*5/100, modal*5/100, modal*3/100]
bulan=0
sum=0

print("Modal awal pengusaha :",modal)
print()
for i in laba:
    sum=0+i
    bulan+=1
    print("Laba pada bulan ke-",bulan,"mendapat laba: ",i)
print("Total laba adalah: ",sum)
