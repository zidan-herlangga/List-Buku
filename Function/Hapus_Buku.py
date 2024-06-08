from .Banner import banner
from os import system, name

def clear_screen():
    system("cls" if name == "nt" else "clear")

def hapus_buku(daftar_buku):
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
