from .Banner import banner

import os

def tampilkan_daftar(daftar_buku):
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    
    print("\nDaftar Buku:")
    for idx, buku in enumerate(daftar_buku, 1):
        # print(f"{idx}. {buku[0]} | {buku[1]} | {buku[2]}\n")
        print(f"{idx}. {buku[0]}")


    while True:
        if not daftar_buku:
            print("\nBuku tidak tersedia.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            os.system("cls" if os.name == "nt" else "clear")
            return
        
        if daftar_buku:
            input("\nTekan Enter untuk kembali ke menu utama...")
            os.system("cls" if os.name == "nt" else "clear")
            return