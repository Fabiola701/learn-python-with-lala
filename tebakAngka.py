import random

def mulai_game():
    angka_rahasia = random.randint(1, 100)
    kesempatan = 10

    print("Selamat datang di Tebak Angka!")
    print("Saya sudah memilih angka dari 1 sampai 100.")
    print("Kamu punya 10 kesempatan untuk menebak.\n")

    while kesempatan > 0:
        tebakan = int(input("Tebak angkanya: "))
        
        if tebakan == angka_rahasia:
            print("🎉 Yeay! Tebakanmu benar!")
            return
        elif tebakan < angka_rahasia:
            print("Terlalu rendah! 📉")
        else:
            print("Terlalu tinggi! 📈")
        
        kesempatan -= 1
        print(f"Sisa kesempatan: {kesempatan}\n")

    print("Sayang sekali, kamu kehabisan kesempatan.")
    print(f"Angka yang benar adalah {angka_rahasia}.")

mulai_game()