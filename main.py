from Function.Banner import banner
from Function.Tambah_Buku import tambah_buku
from Function.Cari_Buku import cari_buku
from Function.Tampilkan_Daftar import tampilkan_daftar
from Function.Hapus_Buku import hapus_buku

from os import system, name 
from time import sleep  

def clear_screen():
    system("cls" if name == "nt" else "clear")

def main():
    clear_screen()

    daftar_buku = []
    
    try:
        while True:
            banner()
            print("\nPilih menu:")
            print("1. Tambah Buku")
            print("2. Cari Buku")
            print("3. Tampilkan Daftar Buku")
            print("4. Hapus Buku")
            print("0. Keluar")
            pilihan = input("\nMasukkan pilihan: ")

            if pilihan == "1":
                tambah_buku(daftar_buku)
            elif pilihan == "2":
                cari_buku(daftar_buku)
            elif pilihan == "3":
                tampilkan_daftar(daftar_buku)
            elif pilihan == "4":
                hapus_buku(daftar_buku)
            elif pilihan == "0":
                print("Terima kasih!")
                break
            else:
                print("\nPilihan tidak valid. Silakan pilih menu yang tersedia.")
                sleep(2)
                clear_screen()
                continue
    
    except KeyboardInterrupt:
        print("\n\nProgram telah berhenti!")

if __name__ == "__main__":
    main()
