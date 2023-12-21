class Maskapai:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_penerbangan = []

    def tambah_penerbangan(self, tujuan, harga):
        penerbangan = {'tujuan': tujuan, 'harga': harga}
        self.daftar_penerbangan.append(penerbangan)

class Pembeli:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []

    def pesan_tiket(self, maskapai, nomor_penerbangan, jumlah_tiket):
        if 1 <= nomor_penerbangan <= len(maskapai.daftar_penerbangan):
            penerbangan_terpilih = maskapai.daftar_penerbangan[nomor_penerbangan - 1]
            total_harga = penerbangan_terpilih['harga'] * jumlah_tiket
            pesanan = {'tujuan': penerbangan_terpilih['tujuan'], 'jumlah_tiket': jumlah_tiket, 'total_harga': total_harga}
            self.pesanan.append(pesanan)
            print(f"Tiket untuk penerbangan ke {penerbangan_terpilih['tujuan']} ({jumlah_tiket} tiket) berhasil dipesan.")
            print(f"Total Harga: Rp{total_harga}")
        else:
            print("Nomor penerbangan tidak valid.")

    def tampilkan_pesanan(self):
        print("\nPesanan Anda:")
        for i, pesanan in enumerate(self.pesanan, start=1):
            print(f"{i}. Tujuan: {pesanan['tujuan']}, Jumlah Tiket: {pesanan['jumlah_tiket']}, Total Harga: Rp{pesanan['total_harga']}")

# Inisialisasi maskapai dan penerbangan
garuda = Maskapai("Garuda Indonesia")
garuda.tambah_penerbangan("Jakarta", 500000)
garuda.tambah_penerbangan("Bali", 800000)
garuda.tambah_penerbangan("Surabaya", 600000)

# Inisialisasi pembeli
pembeli = Pembeli("John Doe")

while True:
    print("\nAplikasi Pembelian Tiket Pesawat:")
    print("1. Lihat Penerbangan")
    print("2. Pesan Tiket")
    print("3. Lihat Pesanan")
    print("0. Keluar")

    pilihan = input("Masukkan nomor pilihan: ")

    if pilihan == '0':
        print("Terima kasih! Selamat tinggal.")
        break
    elif pilihan == '1':
        print("\nDaftar Penerbangan:")
        for i, penerbangan in enumerate(garuda.daftar_penerbangan, start=1):
            print(f"{i}. Tujuan: {penerbangan['tujuan']}, Harga: Rp{penerbangan['harga']}")
    elif pilihan == '2':
        nomor_penerbangan = int(input("Masukkan nomor penerbangan yang ingin dipesan: "))
        jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
        pembeli.pesan_tiket(garuda, nomor_penerbangan, jumlah_tiket)
    elif pilihan == '3':
        pembeli.tampilkan_pesanan()
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
