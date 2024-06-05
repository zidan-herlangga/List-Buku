from time import sleep
from os import system, name


def banner():
    print("=" * 50)
    print("\t        ┓ •    ┳┓  ┓             ")
    print("\t        ┃ ┓┏╋  ┣┫┓┏┃┏┓┏          ")
    print("\t        ┗┛┗┛┗  ┻┛┗┻┛┗┗┻          ")
    print("\t┏┓┳┓┳┓┏┓┓┏  ┳┓┳┳┳┓┏┓┳┓┏┓┳┏┓┳┓┏┓┓ ")
    print("\t┣┫┣┫┣┫┣┫┗┫  ┃┃┃┃┃┃┣ ┃┃┗┓┃┃┃┃┃┣┫┃ ")
    print("\t┛┗┛┗┛┗┛┗┗┛  ┻┛┻┛ ┗┗┛┛┗┗┛┻┗┛┛┗┛┗┗┛")
    print("\t           KELOMPOK 1            ")
    print("=" * 50)

def tambah_buku(daftar_buku):
    system("cls" if name == "nt" else "clear")

    while True:
        banner()
        judul = input("\nMasukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        tahun_terbit = input("Masukkan tahun terbit: ")
        daftar_buku.append([judul, penulis, tahun_terbit])
        
        print("\nBuku berhasil ditambahkan.")
        sleep(1)
        
        continue_ = input("\nIngin tambah buku (y/n)? ")
        
        if continue_.lower() == "y":
            system("cls" if name == "nt" else "clear")
            continue       
        else: 
            system("cls" if name == "nt" else "clear")
            break

def cari_buku(daftar_buku):
    system("cls" if name == "nt" else "clear")
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
        system("cls" if name == "nt" else "clear")
        cari_buku(daftar_buku)
    else:
        system("cls" if name == "nt" else "clear")

def tampilkan_daftar(daftar_buku):
    system("cls" if name == "nt" else "clear")
    banner()
    
    print("\nDaftar Buku:")
    for idx, buku in enumerate(daftar_buku, 1):
        # print(f"{idx}. {buku[0]} | {buku[1]} | {buku[2]}\n")
        print(f"{idx}. {buku[0]}")


    while True:
        if not daftar_buku:
            print("\nBuku tidak tersedia.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            system("cls" if name == "nt" else "clear")
            return
        
        if daftar_buku:
            input("\nTekan Enter untuk kembali ke menu utama...")
            system("cls" if name == "nt" else "clear")
            return

def hapus_buku(daftar_buku):
    
    def clear_screen():
        system("cls" if name == "nt" else "clear")

    clear_screen()
    while True:
        banner()
        print("\nHapus Buku:")
        if not daftar_buku:
            print("\nDaftar buku kosong.")
            input("\nTekan Enter untuk kembali ke menu utama...")
            clear_screen()
            return

        for idx, buku in enumerate(daftar_buku, 1):
            print(f"{idx}. {buku[0]} | {buku[1]} | {buku[2]}")

        try:
            delete = int(input("\nPilih nomor buku yang ingin dihapus (jika tidak ketik '0'): "))

            if delete == 0:
                clear_screen()
                return
            
            if 1 <= delete <= len(daftar_buku):
                del daftar_buku[delete - 1]
                print("\nBuku berhasil dihapus.")
            else:
                print("\nNomor buku tidak tersedia.")
        
        except ValueError:
            print("\nMasukkan nomor yang valid.")
        except IndexError:
            print("\nNomor buku tidak tersedia.")

        continue_ = input("\nIngin menghapus buku lagi (y/n)? ").strip().lower()

        if continue_ == "y":
            clear_screen()
        else:
            clear_screen()
            break

class ListBuku:
    def main():

        system("cls" if name == "nt" else "clear")

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
                    system("cls" if name == "nt" else "clear")
                    continue
        
        except KeyboardInterrupt:
            print("\n\nProgram telah berhenti!")

if __name__ == "__main__":
    LB = ListBuku
    LB.main()