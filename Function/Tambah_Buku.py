from .Banner import banner

import os
import time

def tambah_buku(daftar_buku):
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        banner()

        judul = input("\nMasukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun_terbit = input("Masukkan tahun terbit: ")
        daftar_buku.append([judul, penulis, tahun_terbit])
        
        print("\nBuku berhasil ditambahkan.")
        time.sleep(1)
        
        continue_ = input("\nIngin tambah buku (y/n)? ")
        
        if continue_.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            continue       
        else: 
            os.system("cls" if os.name == "nt" else "clear")
            break