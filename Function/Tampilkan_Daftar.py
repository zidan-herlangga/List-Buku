from .Banner import banner
from os import system, name

def clear_screen():
    system("cls" if name == "nt" else "clear")

def tampilkan_daftar(daftar_buku):
    clear_screen()
    
    banner()
    print("\nDaftar Buku:")
    for idx, buku in enumerate(daftar_buku, 1):
        print(f"{idx}. {buku[0]}")

    while True:
        if not daftar_buku:
            print("\nBuku tidak tersedia.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            clear_screen()
            return
        
        if daftar_buku:
            input("\nTekan Enter untuk kembali ke menu utama...")
            clear_screen()
            return