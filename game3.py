import random

def mulai_game():
    
    # 1. Tentukan level dan angka_rahasia SEBELUM loop
    print("Select your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")
    
    max_num = 10 # Default
    try:
        level = int(input("Enter level (1-3): "))
        if level == 1:
            max_num = 10
        elif level == 2:
            max_num = 100
        elif level == 3:
            max_num = 1000
        else:
            print("Invalid level selected. Defaulting to Easy (1-10).")
            max_num = 10
    except ValueError:
        print("Invalid input. Defaulting to Easy (1-10).")
        max_num = 10

    angka_rahasia = random.randint(1, max_num)
    kesempatan = 10

    # 2. Gunakan 'max_num' agar pesan pembuka sesuai level
    print(f"\nTry to guess the secret number between 1 and {max_num}!")
    print(f"You have {kesempatan} attempts. \n")

    while kesempatan > 0:
        
        # 3. Tambahkan try-except untuk input yang salah
        try:
            tebakan = int(input("Enter your guess: "))
        except ValueError:
            print("That's not a number! Try again.")
            continue # Ulangi loop tanpa mengurangi kesempatan

        # 4. Ini adalah LOGIKA YANG DIPERBAIKI
        if tebakan == angka_rahasia:
            print("You got it!🎉")
            return # Keluar dari fungsi (game selesai)
        elif tebakan < angka_rahasia:
            print("Terlalu rendah! 📉 (Too low!)")
        else:
            print("Terlalu tinggi! 📈 (Too high!)")
        
        kesempatan -= 1
        
        if kesempatan > 0:
            print(f"Remaining attempts: {kesempatan}\n")
        
    # Ini hanya berjalan jika 'while' loop selesai (kesempatan = 0)
    print("\nSorry, you're out of attempts.")
    print(f"The secret number was {angka_rahasia}.")

# Memulai game
mulai_game()