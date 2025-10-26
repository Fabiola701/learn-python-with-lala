# what is looping?
# Looping is used for iterating over a sequence
# perulangan sesuai dengan urutannya

# For
# Else in for lop
# nested loops

# While 
# The Break Statement
# The Continue Statement
# The Else Statement

# misalnya: 1,2,3,4,5,6,7
# seq
# dia berurutan

# for digunakan ketika perulangannya diketahui
# contohnya: 1,2,3
# kita menggunakan for jika rangenya diketahui 
# for akan melihat masing-masing elemen dalam sebuah sequence

for i in range(1, 8):  # akan mengulang dari 1 sampai 7
    print("Perulangan ke-", i)

# while digunakan ketika perulangannya tidak diketahui
# contohnya: user memasukkan angka sampai dia memasukkan angka 0
# kita menggunakan while jika rangenya tidak diketahui
# while akan terus mengulang selama kondisi bernilai True

# contoh for loop
for x in range(6):
    print(x, "\n")

for r in range(2, 6):
    print(r)
print("\n")

for p in range(2, 30, 3):  # start, stop, step
    print(p)
print("\n")

for s in "Indonesia":
    print(s)
print("\n")

for y in range(5,-1,-1):
    print(y)
print("\n")

for u in range(2, 10, 2):
    print(u)
else:
    print("Finish!")

print("\n")

for h in range(1, 10):
    print(h)
    if h == 5:
        break
else:
    print("Selesai")