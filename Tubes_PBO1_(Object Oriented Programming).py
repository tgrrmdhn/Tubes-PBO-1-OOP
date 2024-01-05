import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import secrets
import string

data_busur = {
    'Brand': ['Samick', 'Epic', 'Cartel', 'Wiawis', 'WNS', 'HOYT', 'Elite', 'Sanlida'],
    'Jenis': ['Recurve', 'Standard', 'Standard', 'Recurve', 'Standard', 'Recurve', 'Compound', 'Compound'],
    'Harga': [5500000, 1650000, 1600000, 13500000, 1400000, 14000000, 22500000, 18000000],
    'Stok': [5, 8, 12, 6, 8, 7, 4, 6]
}
df_bsr = pd.DataFrame(data_busur)

data_panah = {
    'Brand': ['Musen', 'Accmoss', 'Platinum', 'Tribute', 'Pandarus', 'X10'],
    'Jenis': ['Aluminium', 'Carbon', 'Aluminium', 'Aluminium', 'Carbon', 'Carbon'],
    'Harga': [50000, 65000, 150000, 100000, 90000, 575000],
    'Stok': [45, 64, 56, 48, 49, 32]
}
df_pnh = pd.DataFrame(data_panah)

data_transaksi = [] 

class Panahan():
    def __init__(self, brand):
        self.brand = brand
        self.jenis = None

    def Ubah(self, mode, **kwargs):
        if mode == 1:
            row_index = df_bsr[df_bsr["Brand"] == self.brand].index
            for column, self.new_value in kwargs.items():
                df_bsr.at[row_index[0],column] = self.new_value
        if mode == 2:
            row_index = df_pnh[df_pnh["Brand"] == self.brand].index
            for column, self.new_value in kwargs.items():
                df_pnh.at[row_index[0],column] = self.new_value
    
    def Tambah(self, mode, *args):
        if mode == 1:
            new_data = {'Brand': self.brand, 'Jenis': args[0], 'Harga': args[1], 'Stok': args[2]}
            df_bsr.loc[len(df_bsr)] = new_data
            print(f"Data Busur {self.brand} berhasil ditambahkan.")
        elif mode == 2:
            new_data = {'Brand': self.brand, 'Jenis': args[0], 'Harga': args[1], 'Stok': args[2]}
            df_pnh.loc[len(df_pnh)] = new_data
            print(f"Data Panah {self.brand} berhasil ditambahkan.")

class Busur(Panahan):
    def __init__(self, brand, jumlah):
        super().__init__(brand)
        self.jumlah = jumlah
        for i in range(len(df_bsr)):
            if df_bsr.at[i, 'Brand'] == self.brand:
                self.jenis = df_bsr.at[i, 'Jenis']
        self._harga = 0
        self.__stok = 0

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, value):
        self._harga = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        self.__stok = value

    def hitung(self):
        for i in range(len(df_bsr)):
            if df_bsr.at[i, 'Brand'] == self.brand:
                self.hrg = self._harga * self.jumlah
                self.stk = df_bsr.at[i, 'Stok'] - self.jumlah
                df_bsr.at[i, 'Stok'] = self.stk
        self.alphabet = string.ascii_letters + string.digits
        self.kode = ''.join(secrets.choice(self.alphabet) for i in range(10))

    def tampil(self):
        global data_transaksi, df_trs
        data_transaksi.append({
            'Kode Transaksi': self.kode,
            'Brand': self.brand,
            'Jenis': self.jenis,
            'Jumlah': self.jumlah,
            'Harga': self.hrg
        })
        df_trs = pd.DataFrame(data_transaksi)
        print(df_trs)

class Panah(Panahan):
    def __init__(self, brand, jumlah):
        super().__init__(brand)
        self.jumlah = jumlah
        for i in range(len(df_pnh)):
            if df_pnh.at[i, 'Brand'] == self.brand:
                self.jenis = df_pnh.at[i, 'Jenis']
        self._harga = 0
        self.__stok = 0

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, value):
        self._harga = value

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, value):
        self.__stok = value

    def hitung(self):
        for i in range(len(df_pnh)):
            if df_pnh.at[i, 'Brand'] == self.brand:
                self.hrg = self._harga * self.jumlah
                self.stk = df_pnh.at[i, 'Stok'] - self.jumlah
                df_pnh.at[i, 'Stok'] = self.stk
        self.alphabet = string.ascii_letters + string.digits
        self.kode = ''.join(secrets.choice(self.alphabet) for i in range(10))

    def tampil(self):
        global data_transaksi, df_trs
        data_transaksi.append({
            'Kode Transaksi': self.kode,
            'Brand': self.brand,
            'Jenis': self.jenis,
            'Jumlah': self.jumlah,
            'Harga': self.hrg
        })
        df_trs = pd.DataFrame(data_transaksi)
        print(df_trs)

def About():
    req = requests.get('https://id.wikipedia.org/wiki/Panahan')
    soup = BeautifulSoup(req.content, 'html.parser')
    content = soup.find('p')
    print(content.get_text())

def File(mode):
    if mode == 1:
        df_bsr.to_csv('Busur.csv', index=False)
        new_df = pd.read_csv('Busur.csv')
        print(new_df)
    elif mode == 2:
        df_pnh.to_csv('Panah.csv', index=False)
        new_df = pd.read_csv('Panah.csv')
        print(new_df)
    elif mode == 3:
        df_trs = pd.DataFrame(data_transaksi)
        if not df_trs.empty:
            df_trs.to_csv('Transaksi.csv', index=False)
            new_df = pd.read_csv('Transaksi.csv')
            print(new_df)
        else:
            print('Belum ada transaksi yang berjalan')

def MinMaxMean(mode):
    if mode == 1:
        df_sorted = df_bsr.sort_values(by='Jenis', ascending=True)
        min = np.min(df_sorted['Harga'])
        max = np.max(df_sorted['Harga'])
        mean = np.mean(df_sorted['Harga'])
        print("Minimum Harga Busur : ", min)
        print("Maksimal Harga Busur : ", max)
        print("Rata-rata Harga Busur : ", mean)
    elif mode == 2:
        df_sorted = df_pnh.sort_values(by='Jenis', ascending=True)
        min = np.min(df_sorted['Harga'])
        max = np.max(df_sorted['Harga'])
        mean = np.mean(df_sorted['Harga'])
        print("Minimum Harga Busur : ", min)
        print("Maksimal Harga Busur : ", max)
        print("Rata-rata Harga Busur : ", mean)

def Grafik(mode):
    if mode == 1:
        df_sorted = df_bsr.sort_values(by='Jenis', ascending=True)
        plt.title('Stok Busur')
    elif mode == 2:
        df_sorted = df_pnh.sort_values(by='Jenis', ascending=True)
        plt.title('Stok Panah')
    plt.bar(df_sorted['Brand'], df_sorted['Stok'])
    plt.xlabel('Brand')
    plt.ylabel('Stok')
    plt.show()

def Pilihan(pil):
    if pil == 1:
        print('===== Tentang Panahan =====')
        About()
    elif pil == 2:
        print('===== Input dan Baca File =====')
        print('1. Busur')
        print('2. Panah')
        print('3. Transaksi')
        pilihan = int(input("Pilih data yang akan diolah : "))
        File(pilihan)
    elif pil == 3:
        print('===== Beli Busur =====')
        print(df_bsr)
        brand = input('Masukkan Brand Yang Anda Inginkan : ')
        jml = int(input('Masukkan Jumlah Barang Yang Ingin Dibeli : '))
        for i in range(len(df_bsr)):
            if df_bsr.at[i, 'Brand'] == brand:
                harga = df_bsr.at[i, 'Harga']
                stok = df_bsr.at[i, 'Stok']
        busur = Busur(brand, jml)
        busur.harga = harga
        busur.stok = stok
        busur.hitung()
        busur.tampil()
    elif pil == 4:
        print('===== Beli Panah =====')
        print(df_pnh)
        brand = input('Masukkan Brand Yang Anda Inginkan : ')
        jml = int(input('Masukkan Jumlah Barang Yang Ingin Dibeli : '))
        for i in range(len(df_pnh)):
            if df_pnh.at[i, 'Brand'] == brand:
                harga = df_pnh.at[i, 'Harga']
                stok = df_pnh.at[i, 'Stok']
        panah = Panah(brand, jml)
        panah.harga = harga
        panah.stok = stok
        panah.hitung()
        panah.tampil()
    elif pil == 5:
        print('===== Grafik Stok =====')
        print('1. Busur')
        print('2. Panah')
        pilihan = int(input("Pilih data yang akan ditampilkan : "))
        Grafik(pilihan)
    elif pil == 6:
        print('===== Nilai Minimal, Maksimal, dan Rata-rata Harga =====')
        print('1. Busur')
        print('2. Panah')
        pilihan = int(input("Pilih data yang akan ditampilkan : "))
        MinMaxMean(pilihan)
    elif pil == 7:
        print('===== Ubah Data =====')
        print('1. Busur')
        print('2. Panah')
        pilihan = int(input("Pilih data yang akan diubah : "))
        print(df_bsr)
        brand = input('Pilih brand yang akan diganti datanya : ')
        hrg = int(input('Masukkan harga baru : '))
        stk = int(input('Masukkan stok baru : '))
        obj = Panahan(brand)
        obj.Ubah(pilihan, Harga=hrg, Stok=stk)
    elif pil == 8:
        print('===== Penambahan Data =====')
        print('1. Busur')
        print('2. Panah')
        pilihan = int(input("Pilih data yang akan ditambahkan : "))
        brand = input('Masukkan brand : ')
        jenis = input('Masukkan jenis : ')
        harga = int(input('Masukkan harga : '))
        stok = int(input('Masukkan stok : '))
        tambah = Panahan(brand)
        tambah.Tambah(pilihan, jenis, harga, stok)

if __name__ == '__main__':
    pil = 0
    print('===== Selamat Datang di Toko Archertech =====')
    while pil != 9:
        print('===== Pilihan =====')
        print('1. Tentang Panahan')
        print('2. Olah File')
        print('3. Beli Busur')
        print('4. Beli Panah')
        print('5. Grafik Stok')
        print('6. Nilai Minimal, Maksimal, dan Rata-rata Harga')
        print('7. Ubah Data')
        print('8. Tambah Data')
        print('9. Keluar Program')
        pil = int(input('Silakan masukkan pilihan anda : '))
        Pilihan(pil)
    print('===== Terima Kasih =====')

    