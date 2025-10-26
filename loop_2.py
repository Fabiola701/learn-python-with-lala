for a in range(1, 5):
    for b in range(a):
        print(a, end=" ")
    print()

print("\n--- while loop ---")

i = 1
while i < 6:
    print(i)
    i += 1

print("\n--- nested while loop ---")
m = 1
while m <= 3:
    n = 1
    while n <= 4:
        print("x", end=" ")
        n += 1
    print()
    m += 1