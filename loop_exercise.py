print("--- Menampilkan angka genap dari 1 sampai 100 ---")
print("\n")

for i in range (1, 101):
    if i % 2 == 0:
        print(i)
else:
    print("Tidak ada angka genap")

# for k in range(2, 101, 2):
#     print(k)

print("\n")

count = 0
for t in range(1, 101):
   if t % 2 == 0:
       count += 1
print("Jumlah angka genap dari 1 sampai 100 adalah:", count)

print("\n--- Menampilkan ouput yang di slide ---")

for j in range(1, 5):
    print( str(j) * j)

for a in range(1, 5):
    for b in range(a):
        print(a, end=" ")
    print()
