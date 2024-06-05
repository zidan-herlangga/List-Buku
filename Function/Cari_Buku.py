from .Banner import banner

import os

def cari_buku(daftar_buku):
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    judul = input("\nMasukkan judul buku yang ingin dicari: ")
    
    found = False
    
    for buku in daftar_buku:
        if judul.lower() in buku[0].lower():
            print("\nBuku ditemukan:")
            print("Judul:", buku[0])
            print("Penulis:", buku[1])
            print("Tahun Terbit:", buku[2])
            found = True    
    
    if not found:
        print("\nBuku tidak ditemukan.")

    continue_ = input("\nIngin mencari buku lagi (y/n)? ")
    
    if continue_.lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")
        cari_buku(daftar_buku)
    else:
        os.system("cls" if os.name == "nt" else "clear")