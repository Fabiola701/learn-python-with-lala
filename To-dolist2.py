# 1. Siapkan list kosong untuk menyimpan semua tugas
daftar_tugas = []

print("--- Selamat Datang di Aplikasi To-Do List ---")

# 2. Gunakan loop 'while' agar program terus berjalan
while True:
    print("\nPilihan: [tambah] [lihat] [selesai]")
    pilihan = input("Apa yang ingin kamu lakukan? > ")

    # 3. Gunakan if/elif/else untuk setiap pilihan
    if pilihan == "tambah":
        tugas_baru = input("Masukkan tugas baru: ")
        daftar_tugas.append(tugas_baru)
        print("Tugas berhasil ditambahkan!")

    elif pilihan == "lihat":
        print("\n--- Daftar Tugasmu ---")
        if not daftar_tugas: # Cara keren untuk cek apakah list kosong
            print("(Belum ada tugas)")
        else:
            # 4. Gunakan loop 'for' untuk menampilkan semua item di list
            for tugas in daftar_tugas:
                print(f"- {tugas}")

    elif pilihan == "selesai":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")