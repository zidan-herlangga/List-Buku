from .Banner import banner
from os import system, name
from time import sleep

def clear_screen():
    system("cls" if name == "nt" else "clear")

def tambah_buku(daftar_buku):
    clear_screen()
    
    while True:    
        banner()
        print("\nTambah Buku:")

        try:
            judul = input("\nMasukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            tahun_terbit = input("Masukkan tahun terbit: ")
            daftar_buku.append([judul, penulis, tahun_terbit])

            print("\nBuku berhasil ditambahkan.")
            sleep(1)

        except KeyboardInterrupt:
            clear_screen()
            return
        
        continue_ = input("\nIngin tambah buku (y/n)? ")
        
        if continue_.lower() == "y":
            clear_screen()
            continue       
        else: 
            clear_screen()
            break