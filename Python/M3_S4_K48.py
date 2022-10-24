#Python os module is imported to clear the console screen in any operating system
import os


pakaian = True

while(pakaian):
    print("====================================")
    print("====== K I S I - U N I Q L O ======")
    print("====================================")
    print("")
    print("===== IDENTITAS PELANGGAN =====")
    nama = str(input("Nama \t\t: "))
    alamat = str(input("Alamat \t\t: "))
    nomor_telepon = int(input("Nomor Telepon \t: "))
    print("===============================")
    print("Silakan Pilih Jenis Pakaian\n1. Jaket\n2. Kaos\n3. Celana")
    jenis_pakaian = str(input("Pilih Jenis Pakaian: "))
    if jenis_pakaian == "Jaket" or jenis_pakaian == "1":
        jenis_pakaian = "Jaket"
        print("Pilihan Jaket\n1. Crewneck\n2. Hoodie\n3. Sweater")
        pilihan_jaket = str(input("Pilih Model Jaket: "))
        if pilihan_jaket == "Crewneck" or pilihan_jaket == "1":
            harga = 185000
            pilihan = "Crewneck"
            stok_crewneck = 40
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_crewneck = stok_crewneck - jumlah_pesanan_utama
            stokfix = stokakhir_crewneck
            A = jumlah_pesanan_utama*harga
            hargafix = A
        elif pilihan_jaket == "Hoodie" or pilihan_jaket == "2":
            harga = 155000
            pilihan = "Hoodie"
            stok_hoodie = 10
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_hoodie = stok_hoodie - jumlah_pesanan_utama
            stokfix = stokakhir_hoodie
            B = jumlah_pesanan_utama*harga
            hargafix = B
        elif pilihan_jaket == "Sweater" or pilihan_jaket == "3":
            harga = 175000
            pilihan = "Sweater"
            stok_sweater = 30
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_sweater = stok_sweater - jumlah_pesanan_utama
            stokfix = stokakhir_sweater
            C = jumlah_pesanan_utama*harga
            hargafix = C
        else: 
            print("Maaf, pilihan tidak tersedia")
        
    elif jenis_pakaian == "Kaos" or jenis_pakaian == "2":
        jenis_pakaian = "Kaos"
        print ("Pilihan Kaos\n1.Long\n2. Short\n3. V-Neck")
        pilihan_kaos = str(input("Pilih Model Kaos: "))
        if pilihan_kaos == "Long" or pilihan_kaos == "1":
            harga = 150000
            pilihan = "Long"
            stok_long = 28
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_long = stok_long - jumlah_pesanan_utama
            stokfix = stokakhir_long
            D = jumlah_pesanan_utama*harga
            hargafix = D * 0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        elif pilihan_kaos == "Short" or pilihan_kaos == "2":
            harga = 275000
            pilihan = "Short"
            stok_short = 37
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_short = stok_short - jumlah_pesanan_utama
            stokfix = stokakhir_short
            E = jumlah_pesanan_utama*harga
            hargafix = E * 0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        elif pilihan_kaos == "V-Neck" or pilihan_kaos == "3":
            harga = 260000
            pilihan = "V-Neck"
            stok_v_neck = 26
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_vneck = stok_v_neck - jumlah_pesanan_utama
            stokfix = stokakhir_vneck
            F = jumlah_pesanan_utama*harga
            hargafix = F * 0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        else: 
            print("Maaf, pilihan tidak tersedia")

    elif jenis_pakaian == "Celana" or jenis_pakaian == "3":
        jenis_pakaian = "Celana"
        print ("Pilihan Celana\n1. Jeans\n2. Parka\n3. Chino\n4. Pendek")
        pilihan_celana = str(input("Pilih Model Celana: "))
        if pilihan_celana == "Jeans" or pilihan_celana == "1":
            harga = 380000
            pilihan = "Jeans"
            stok_jeans = 19
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_jeans = stok_jeans - jumlah_pesanan_utama
            stokfix = stokakhir_jeans
            G = jumlah_pesanan_utama*harga
            hargafix = G *0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        elif pilihan_celana == "Parka" or pilihan_celana == "2":
            harga = 290000
            pilihan = "Parka"
            stok_parka = 39
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_parka = stok_parka - jumlah_pesanan_utama
            stokfix = stokakhir_parka
            H = jumlah_pesanan_utama*harga
            hargafix = H*0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        elif pilihan_celana == "Chino" or pilihan_celana == "3":
            harga = 270000
            pilihan = "Chino"
            stok_chino = 16
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_chino = stok_chino - jumlah_pesanan_utama
            stokfix = stokakhir_chino
            I = jumlah_pesanan_utama*harga
            hargafix = I*0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        elif pilihan_celana == "Pendek" or pilihan_celana == "4":
            harga = 155000
            pilihan = "Pendek"
            stok_pendek = 34
            jumlah_pesanan_utama = int(input("Jumlah Pesanan: "))
            stokakhir_pendek = stok_pendek - jumlah_pesanan_utama
            stokfix = stokakhir_pendek
            J = jumlah_pesanan_utama*harga
            hargafix = J*0.5 #diskon 50%
            print("Selamat anda mendapatkan diskon 50%")
        else: 
            print("Maaf, pilihan tidak tersedia")
    else: 
        print("Maaf, jenis pakaian tidak tersedia")

    print("\n")
    print("Apakah ada produk tambahan?\n1. Kaos Kaki\n2. Kaca Mata\n3. Tidak")
    produk_tambahan = str(input("Masukan Pilihan: "))
    if produk_tambahan == "Kaos Kaki" or produk_tambahan == "1":
            produk_tambahan = "Kaos Kaki"
            harga = 70000
            stok_kaos_kaki = 25
            jumlah_pesanan_tambahan = int(input("Jumlah Pesanan: "))
            stokakhir_kaoskaki = stok_kaos_kaki - jumlah_pesanan_tambahan
            stokfixtambahan = stokakhir_kaoskaki
            K = jumlah_pesanan_tambahan*harga
            hargafix2 = K
            print ("Stok Produk : ",stokfixtambahan)
    elif produk_tambahan == "Kaca Mata" or produk_tambahan == "2":
            produk_tambahan = "Kaca Mata"
            harga = 50000
            stok_kaca_mata = 33
            jumlah_pesanan_tambahan = int(input("Jumlah Pesanan: "))
            stokakhir_kacamata = stok_kaca_mata - jumlah_pesanan_tambahan
            stokfixtambahan = stokakhir_kacamata
            L = jumlah_pesanan_tambahan*harga
            hargafix2 = L
            print ("Stok produk tambahan yang dipesan: ",stokfixtambahan)
    elif produk_tambahan == "Tidak" or produk_tambahan == "3":
        print("Terima kasih, telah membeli")
    else: print("Maaf, produk tambahan tidak tersedia")
    print ("Stok jenis pakaian yang dipesan: ",stokfix)

    subtotal = hargafix + hargafix2
    print ("Subtotal: ", subtotal)


    #PROSES
    pajak_member = subtotal*0.1
    pajak_nonmember = subtotal*0.14
    total_member = subtotal + pajak_member
    subtotal_nonmember1 = subtotal + pajak_member + 15000
    subtotal_nonmember2 = subtotal + pajak_nonmember
    total_transaksi = subtotal_nonmember1
    total_transaksi = subtotal_nonmember2
    total_transaksi = total_member
    potongan = total_transaksi*0.1
    total_potongan = total_transaksi - potongan
    total_cashback = total_transaksi + potongan

    print("\n")
    print("Apakah anda memiliki member?\n1. Ya\n2. Tidak")
    status_member = str(input("Pelanggan memiliki member? "))
    if status_member == "Ya" or status_member == "1":
        print("Subtotal: ",total_member)
        status_member = "Member"
    elif status_member == "Tidak" or status_member == "2":
        print("Apakah Anda ingin membuat member?\n1. Ya\n2. Tidak")
        tawaran_member = str(input("Ingin membuat member?"))
        if tawaran_member == "Ya" or tawaran_member == "1":
            print("Biaya pendaftaran member sebesar Rp15.000")
            print("Subtotal: ",subtotal_nonmember1)
            status_member = "Member"
        elif tawaran_member == "Tidak" or tawaran_member == "2":
            print("Subtotal: ",subtotal_nonmember2)
            status_member = "Tidak"
        else:
            print("Pilihan tidak tersedia")
    else:
        print("Pilihan tidak tersedia")
        
    print("\n")

    print("Pembayaran Melalui\n1. Cash\n2. Debit")
    pembayaran = str(input("Metode pembayaran: "))
    if pembayaran == "Cash" or pembayaran == "1":
        if total_transaksi >= 700000: 
            print("Total Transaksi: ", total_potongan)
        elif total_transaksi < 700000:
            print("Total Transaksi: ", round(total_transaksi))
        pembayaran = "Cash"
    elif pembayaran == "Debit" or pembayaran == "2":
        print("Total Transaksi: ", total_cashback)
        pembayaran = "Debit"
    else: ("Not Found")
    
    uang = (int(input("Masukakan Uang Anda \t: ")))
    kembalian = total_transaksi - uang

    os.system('cls') #Sebelum Output Clear Console Dulu
    
    #OUTPUT
    print("=========================================")
    print("=========    STRUK PEMBELIAN    =========")
    print("=========================================")
    print("Nama Pembeli \t\t\t: ", nama)
    print("Status Member \t\t\t: ", status_member)
    print("Alamat Pembeli \t\t\t: ",alamat)
    print("Nomer Telepon \t\t\t: ",nomor_telepon)
    print("Jenis Pakaian \t\t\t: ",jenis_pakaian)
    print("Pilihan Pesanan \t\t: ",pilihan)
    print("Banyak Pesanan \t\t\t: ",jumlah_pesanan_utama)
    print("Produk lain \t\t\t: ",produk_tambahan)
    print("Jumlah Pesanan Produk Lain \t: ",jumlah_pesanan_tambahan)
    print("Casback \t\t\t: " ) #aku gatau variabel cashback yang bener yang kamu yang mana
    print("Potongan Harga \t\t\t: ",round(potongan))
    print("Pajak \t\t\t\t: ",round(pajak_member) or round(pajak_nonmember))
    print("Jenis Pembayaran \t\t: ",pembayaran)
    print("Total Transaksi \t\t: ", round(total_transaksi))

    print("==========================================")

    pecahan_50k = kembalian//50000
    pecahan_20k = kembalian%50000//20000
    pecahan_10k = kembalian%50000%20000//10000
    pecahan_5k = kembalian%50000%20000%10000//5000
    pecahan_1k = kembalian%50000%20000%10000%5000//1000
    pecahan_500 = kembalian%50000%20000%10000%5000%1000//500
    print("Pecahan kembalian yang dibutuhkan: ")
    print("Pecahan 50000\t\t:",round(pecahan_50k))
    print("Pecahan 20000\t\t:",round(pecahan_20k))
    print("Pecahan 10000\t\t:",round(pecahan_10k))
    print("Pecahan 5000\t\t:",round(pecahan_5k))
    print("Pecahan 1000\t\t:",round(pecahan_1k))
    print("Pecahan 500\t\t:",round(pecahan_500))    



    #PROGRAM AKAN KEMBALI DARI AWAL JIKA PELANGGAN INGIN BERBELANJA KEMBALI
    print("\n")
    print("Apakah anda ingin berbelanja kembali?\n1. Ya\n2. Tidak")
    tambahan = str(input("Masukan Pilihan: "))
    if tambahan == "Ya" or tambahan == "1":
        pakaian  = True
        print ("Subtotal: ", subtotal)
        os.system('cls') #fungsi untuk clearscreen console
    elif tambahan == "Tidak" or tambahan == "2":
        pakaian = False
        print("Terima kasih, telah membeli")
    else: 
        print ("Maaf, pilihan tidak tersedia")
        pakaian = False
        print("Terima kasih, telah membeli")
