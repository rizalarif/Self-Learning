print("==========================================")
print("                WELCOME                   ")
print("               KISI-DRINK                 ")
print("==========================================")
print("               OUR MENU                   ")
print("==========================================")
print("\n")
print("     Menu          Ukuran       Harga ")
print("1. Jus Alpukat     Large      Rp20.000")
print("2. Jus Alpukat     Medium     Rp18.000")
print("3. Jus Nanas       Large      Rp20.000")
print("4. Jus Nanas       Medium     Rp17.000")
print("5. Matcha          Large      Rp28.000")
print("6. Matcha          Medium     Rp20.000")
print("7. Thai-Tea        Large      Rp25.000")
print("8. Thai-Tea        Medium     Rp18.000")
print("9. Kopi Susu       Large      Rp26.000")
print("10. Americano      Small      Rp30.000")
print("\n")
print("=============IDENTITAS PELANGGAN==================")
Nama = str(input("Nama\t\t\t\t: "))
Alamat = str(input("Alamat\t\t\t\t: "))
Nomor_Telepon = int(input("Nomor Telepon\t\t\t: "))
Umur = int(input("Umur\t\t\t\t: "))
Tanggal_Lahir = str(input("Tanggal Lahir (DD-MM-YYYY)\t: "))
print("===================================================")
print("\n")
minuman = True

while(minuman):
    print("Pilih Jenis Minuman Yang Akan Dipesan\n1. Jus\n2. Non-Coffee\n3. Coffee")
    jenis_minuman = str(input("Masukan Jenis Minuman: "))
    if jenis_minuman == "Jus" or jenis_minuman == "1":
        print("\n")
        print("Pilih Varian Rasa\n1. Alpukat\n2. Nanas")
        Varian_Rasa = str(input("Masukan Varian Rasa: "))
        if Varian_Rasa == "Alpukat" or Varian_Rasa == "1":
            print("\n")
            print("Pilih Ukuran Minuman\n1. Large\n2. Medium")
            Ukuran_Minuman = int(input("Masukan Ukuran Minuman:  "))
            if Ukuran_Minuman == 1:
                Ukuran = "Large"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 20000
                Total = Harga*Jumlah_Pesanan
            elif Ukuran_Minuman == 2:
                Ukuran = "Medium"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 18000
                Total = Harga*Jumlah_Pesanan
            print("Anda memesan Minuman Jus Alpukat dengan ukuran", Ukuran)
            print("Total = Rp", Total)
        elif Varian_Rasa == "Nanas" or Varian_Rasa == "2":
            print("\n")
            print("Pilih Ukuran Minuman\n1. Large\n2. Medium")
            Ukuran_Minuman = int(input("Masukan Ukuran Minuman: "))
            if Ukuran_Minuman == 1:
                Ukuran = "Large"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 20000
                Total = Harga*Jumlah_Pesanan
            elif Ukuran_Minuman == 2:
                Ukuran = "Medium"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 17000
                Total = Harga*Jumlah_Pesanan
            print("Anda memesan Minuman Jus Nanas dengan ukuran", Ukuran)
            print("Total = Rp", Total)
            if Jumlah_Pesanan >= 3:
                print("Selamat anda mendapatkan bonus voucher untuk pembelian selanjutnya Rp10.000")
            if Jumlah_Pesanan >= 2:
                print("Selamat Anda mendapatkan gelang gratis")

    elif jenis_minuman == "Non-Coffee" or jenis_minuman == "2":
        print("\n")
        print("Pilih Varian Rasa\n1. Matcha\n2. Thai-Tea")
        Varian_Rasa = str(input("Masukan Varian Rasa: "))
        if Varian_Rasa == "Matcha" or Varian_Rasa == "1":
            print("\n")
            print("Pilih Ukuran Minuman\n1. Large\n2. Medium")
            Ukuran_Minuman = int(input("Masukan Ukuran Minuman:  "))
            if Ukuran_Minuman == 1:
                Ukuran = "Large"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 28000
                Total = Harga*Jumlah_Pesanan
            elif Ukuran_Minuman == 2:
                Ukuran = "Medium"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 20000
                Total = Harga*Jumlah_Pesanan
            print("Anda memesan Minuman Matcha dengan ukuran", Ukuran)
            print("Total = Rp", Total)
            if Jumlah_Pesanan >= 2:
                print("Selamat anda mendapatkan bonus voucher pembelian selanjutnya sebesar Rp10.000")
        elif Varian_Rasa == "Thai-Tea" or Varian_Rasa == "2":
            print("\n")
            print("Pilih Ukuran Minuman\n1. Large\n2. Medium")
            Ukuran_Minuman = int(input("Masukan Ukuran Minuman: "))
            if Ukuran_Minuman == 1:
                Ukuran = "Large"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 25000
                Total = Harga*Jumlah_Pesanan
            elif Ukuran_Minuman == 2:
                Ukuran = "Medium"
                Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
                Harga = 18000
                Total = Harga*Jumlah_Pesanan
            print("Anda memesan Minuman Thai-Tea dengan ukuran", Ukuran)
            print("Total = Rp", Total)
    elif jenis_minuman == "Coffee" or jenis_minuman == "3":
        print("\n")
        print("Pilih Varian Rasa\n1. Kopi Susu (Large)\n2. Americano (Small)")
        Varian_Rasa = str(input("Masukan Varian Rasa: "))
        if Varian_Rasa == "Kopi Susu" or Varian_Rasa == "1":
            Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
            Harga = 26000
            Total = Harga*Jumlah_Pesanan
            print("Anda memesan Kopi Susu dengan ukuran Large")
            print("Total = Rp", Total)
        if Varian_Rasa == "Americano" or Varian_Rasa == "2":
            Jumlah_Pesanan = int(input("Jumlah Pesanan: "))
            Harga = 30000
            Total = Harga*Jumlah_Pesanan
            print("Anda memesan Americano dengan ukuran Small")
            print("Total = Rp", Total)

    print("Pilihan anda\n1. Masih ada\n2. tidak ada")
    pilihan = str(input("Apakah ada pesanan lain ? "))

    if pilihan == "Masih ada" or pilihan == "1":
        minuman = True

    elif pilihan == "tidak ada" or pilihan == "2":
        minuman = False
        print("Terimakasih Sudah Memilih Pesanan")
    else:
        print("Maaf, untuk saaat ini pesanan Anda tidak tersedia")
        minuman = False

#PROSES
Diskon_NonMember = Total*0.05
Harga_Setelah_Diskon = Total - Diskon_NonMember
Pajak = Harga_Setelah_Diskon*0.10
Total_Transaksi_Member = Total + Pajak
Total_Transaksi_NonMember = Harga_Setelah_Diskon + Pajak

print("Total Harga: ", Total)
uang_anda = int(input("Cash: Rp"))
Kembalian1 = uang_anda - Total_Transaksi_Member
Kembalian2 = uang_anda - Total_Transaksi_NonMember
print("Ada member card?\n1. Ya\n2. Tidak")
member_card = str(input("Apakah Anda mempunyai member card?"))
if  member_card == "Ya" or member_card == "1":
    print("Total Harga: ", Total_Transaksi_Member)
    if Total_Transaksi_Member >= 200000:
        print("Anda mendapatkan cashback")
        Kembalianfix = Kembalian1
    elif Total_Transaksi_Member <= 200000:
        print("Tidak mendapatkan cashback")
        Kembalianfix = Kembalian1
elif member_card == "Tidak" or member_card == "2":
    if Total_Transaksi_NonMember >= 300000:
        print("Anda mendapatkan diskon sebesar 5%: ", Diskon_NonMember)
        print("Pajak\t:", Pajak)
        print("Total Harga: ", round(Total_Transaksi_NonMember))
        Kembalianfix = Kembalian2
    elif Total_Transaksi_Member <= 300000:
        print("Diskon\t: -")
        print("Pajak\t:", Pajak)
        print("Total Harga\t: ", Total_Transaksi_Member)
        Kembalianfix = Kembalian1
else:
    print("Maaf, total pembelian Anda tidak memenuhi S&K berlaku")

pecahan_50k = Kembalianfix//50000
pecahan_20k = Kembalianfix%50000//20000
pecahan_10k = Kembalianfix%50000%20000//10000
pecahan_5k = Kembalianfix%50000%20000%10000//5000
pecahan_1k = Kembalianfix%50000%20000%10000%5000//1000
pecahan_500 = Kembalianfix%50000%20000%10000%5000%1000//500
print("Pecahan kembalian yang dibutuhkan: ")
print("Pecahan 50000\t\t:",round(pecahan_50k))
print("Pecahan 20000\t\t:",round(pecahan_20k))
print("Pecahan 10000\t\t:",round(pecahan_10k))
print("Pecahan 5000\t\t:",round(pecahan_5k))
print("Pecahan 1000\t\t:",round(pecahan_1k))
print("Pecahan 500\t\t:",round(pecahan_500))    