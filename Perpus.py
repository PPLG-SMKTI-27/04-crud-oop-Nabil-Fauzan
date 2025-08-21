from datetime import datetime

# Class Buku
class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def __str__(self):
        return f"{self.isbn}\t{self.judul}\t{self.pengarang}\t{self.jumlah}\t{self.terpinjam}"

# Class Peminjaman
class Peminjaman:
    def __init__(self, isbn, status, tanggal_pinjam, tanggal_kembali=""):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def __str__(self):
        return f"{self.isbn}\t{self.status}\t{self.tanggal_pinjam}\t{self.tanggal_kembali}"


# Data awal
books = [
    Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15, 0),
    Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, 1),
    Buku("9786022912828", "Animal Farm", "George Orwell", 4, 0),
]

records = [
    Peminjaman("9786022912828", "Selesai", "2025-03-21", "2025-03-28"),
    Peminjaman("9786026163905", "Belum", "2025-07-22", ""),
]

# Fungsi
def bersih():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def tampil():
    print("===== Daftar Buku =====")
    print("No\tISBN\t\t\tJudul\t\t\t\tPengarang\t\tJumlah\tTerpinjam")
    for i, b in enumerate(books):
        print(f"{i+1}\t{b}")
    print("=" * 100)

def tambah_data():
    print("===== Tambah Buku =====")
    isbn = input("ISBN: ")
    judul = input("Judul: ")
    pengarang = input("Pengarang: ")
    jumlah = int(input("Jumlah: "))
    terpinjam = int(input("Terpinjam: "))
    buku_baru = Buku(isbn, judul, pengarang, jumlah, terpinjam)
    books.append(buku_baru)
    print("Buku berhasil ditambahkan.\n")

def edit_data():
    tampil()
    id = int(input("Pilih nomor buku yang ingin diedit: ")) - 1
    if 0 <= id < len(books):
        books[id].isbn = input("ISBN baru: ")
        books[id].judul = input("Judul baru: ")
        books[id].pengarang = input("Pengarang baru: ")
        books[id].jumlah = int(input("Jumlah baru: "))
        books[id].terpinjam = int(input("Terpinjam baru: "))
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")

def hapus_data():
    tampil()
    id = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
    if 0 <= id < len(books):
        del books[id]
        print("Buku berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

def tampilkan_peminjaman():
    print("===== Data Peminjaman =====")
    print("No\tISBN\t\tStatus\tTanggal Pinjam\tTanggal Kembali")
    for i, r in enumerate(records):
        print(f"{i+1}\t{r}")
    print("=" * 100)

def tampilkan_belum():
    print("===== Buku Belum Dikembalikan =====")
    j = 1
    ditemukan = False
    for r in records:
        if r.status.lower() == "belum":
            print(f"{j}\t{r}")
            j += 1
            ditemukan = True
    if not ditemukan:
        print("Semua buku sudah dikembalikan.")
    print("=" * 100)

def peminjaman():
    print("===== Tambah Peminjaman =====")
    isbn = input("ISBN buku: ")
    status = "Belum"
    tanggal_pinjam = input("Tanggal Pinjam (YYYY-MM-DD): ")
    peminjaman_baru = Peminjaman(isbn, status, tanggal_pinjam)
    records.append(peminjaman_baru)
    for b in books:
        if b.isbn == isbn:
            b.terpinjam += 1
            break
    print("Data peminjaman ditambahkan.")

def pengembalian():
    tampilkan_belum()
    idx = int(input("Pilih nomor peminjaman untuk dikembalikan: ")) - 1
    belum_kembali = [r for r in records if r.status == "Belum"]
    if 0 <= idx < len(belum_kembali):
        record = belum_kembali[idx]
        record.status = "Selesai"
        record.tanggal_kembali = input("Tanggal kembali (YYYY-MM-DD): ")
        for b in books:
            if b.isbn == record.isbn:
                b.terpinjam -= 1
                break
        print("Buku berhasil dikembalikan.")
    else:
        print("Indeks tidak valid.")

# Menu utama
while True:
    print("\n---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    bersih()

    if menu == "1":
        tampil()
    elif menu == "2":
        tambah_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        hapus_data()
    elif menu == "5":
        tampilkan_peminjaman()
    elif menu == "6":
        tampilkan_belum()
    elif menu == "7":
        peminjaman()
    elif menu == "8":
        pengembalian()
    elif menu.lower() == "x":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
