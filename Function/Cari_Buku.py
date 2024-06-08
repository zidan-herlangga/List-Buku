from .Banner import banner
from os import system, name

def clear_screen():
    system("cls" if name == "nt" else "clear")

def cari_buku(daftar_buku):
    clear_screen()
    
    banner()
    print("\nCari Buku:")

    try:
        judul = input("\nMasukkan judul buku yang ingin dicari: ")

    except KeyboardInterrupt:
        clear_screen()
        return
    
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
        clear_screen()
        cari_buku(daftar_buku)
    else:
        clear_screen()