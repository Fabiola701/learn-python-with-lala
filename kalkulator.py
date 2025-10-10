x = float(input("Angka 1: "))
op = input("Operasi (+, -, *, /): ")
y = float(input("Angka 2: "))

if op == '+':
    print("Hasil:", x + y)
elif op == '-':
    print("Hasil:", x - y)
elif op == '*':
    print("Hasil:", x * y)
elif op == '/':
    print("Hasil:", "Tidak bisa dibagi dengan nol" if y == 0 else x / y)
else:
    print("Operasi tidak dikenal")
