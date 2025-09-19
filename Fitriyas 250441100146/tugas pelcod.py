import math

def hitung_durasi_tv_series():
    """Menghitung total durasi menonton TV series dalam jam."""
    durasi_per_episode_menit = 35
    total_episode = 10
    total_durasi_menit = durasi_per_episode_menit * total_episode
    total_durasi_jam = total_durasi_menit / 60
    print(f"Total durasi menonton TV series: {total_durasi_jam:.2f} jam")

def hitung_sisa_uang():
    """Menghitung sisa uang setelah membeli ikan."""
    nim_input = input("Masukkan 3 angka terakhir NIM: ")
    try:
        nim = int(nim_input)
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka.")
        return

    uang_bawaan = (nim + 100) * 1000
    harga_cupang = 10000
    harga_koi = 20000
    jumlah_cupang = 5
    jumlah_koi = 2
    total_biaya = (jumlah_cupang * harga_cupang) + (jumlah_koi * harga_koi)
    sisa_uang = uang_bawaan - total_biaya

    print(f"Uang yang Anda bawa: Rp.{uang_bawaan:,}")
    print(f"Total biaya pembelian ikan: Rp.{total_biaya:,}")
    print(f"Sisa uang Anda: Rp.{sisa_uang:,}")

def hitung_biaya_bensin():
    """Menghitung biaya bensin untuk perjalanan."""
    nim_input_3_digit = input("Masukkan 3 angka terakhir NIM (jarak perjalanan): ")
    nim_input_1_digit = input("Masukkan 1 angka terakhir NIM (kapasitas tangki): ")
    try:
        jarak_perjalanan = int(nim_input_3_digit)
        kapasitas_tangki = int(nim_input_1_digit)
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka.")
        return

    harga_bensin_dasar = 1000 + int(nim_input_3_digit)
    konsumsi_bbm = 2.7
    diskon_per_liter = 500

    total_bensin_liter = jarak_perjalanan / konsumsi_bbm
    harga_bensin_setelah_diskon = harga_bensin_dasar
    if total_bensin_liter > 3:
        harga_bensin_setelah_diskon -= diskon_per_liter

    total_biaya = total_bensin_liter * harga_bensin_setelah_diskon
    prakiraan_isi_bensin = math.ceil(total_bensin_liter / kapasitas_tangki)

    print("\n--- Rincian Biaya Bensin ---")
    print(f"Total bensin yang dibutuhkan: {total_bensin_liter:.2f} Liter")
    print(f"Harga bensin per liter setelah diskon: Rp.{harga_bensin_setelah_diskon:,}")
    print(f"Total biaya bensin: Rp.{total_biaya:,.2f}")
    print(f"Prakiraan berapa kali mengisi bensin: {prakiraan_isi_bensin} kali")

# Panggil fungsi untuk menjalankan setiap soal
print("--- Soal 1 ---")
hitung_durasi_tv_series()

print("\n--- Soal 2 ---")
hitung_sisa_uang()

print("\n--- Soal 3 ---")
hitung_biaya_bensin()