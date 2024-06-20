import os
from time import sleep

a ='\033[92m'  # Warna hijau
b ='\033[91m'  # Warna merah
c ='\033[0m'   # Reset warna
os.system('clear')  # Membersihkan layar

print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  Bye:   Kumpulan Remaja')
print('\t web : Kumpulanremaja.com')
print('\t Facebook : fb.me/4Kumpulanremaja')
print('\t Github : https://github.com/kumpulanremaja')
print(a+'+'*40)
print('\nProses..')
sleep(1)

print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
    os.mkdir('/data/data/com.termux/files/home/.termux')
    print(a+'[!] Direktori .termux berhasil dibuat')
except FileExistsError:
    print(a+'[!] Direktori .termux sudah ada')
except Exception as e:
    print(b+f'[!] Kesalahan saat membuat direktori: {e}')
    exit(1)

print(b+'\n[!] Menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
try:
    with open('/data/data/com.termux/files/home/.termux/termux.properties', 'w') as kontol:
        kontol.write(key)
    print(a+'[!] Konfigurasi tombol tambahan berhasil ditulis')
except Exception as e:
    print(b+f'[!] Kesalahan saat menulis konfigurasi: {e}')
    exit(1)

sleep(1)
print(a+'[!] Memproses  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar')
sleep(2)

# Memuat ulang pengaturan Termux
reload_status = os.system('termux-reload-settings')
if reload_status == 0:
    print(a+'[!] Pengaturan Termux berhasil dimuat ulang')
else:
    print(b+'[!] Gagal memuat ulang pengaturan Termux')

print(a+'[!] Proses Selesai !! ^^'+c+'\n\nhubungi : saya lewat Web atau Fanspage Facebook*\n\n')
