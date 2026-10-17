def penjumlahan (a, b):
    return a + b
def pengurangan (a, b):
    return a - b
def perkalian (a, b):
    return a * b
def pembagian (a, b):
    if b !=0:
        return a/b
    else :
        return ("pembagian tidak bisa menggunakan 0")
    
    print ("----kalkulator by harya")
    print ("-----------------------")

    while True:
        print ("Pilih operasi :")
        print ("1. Penjumlahan :")
        print ("2. pengurangan :")
        print ("3. perkalian :")
        print ("4. pembagian :")
        print ("5. keluar :")

        pilihan = input("masukkan pilihan 1/2/3/4/5")

        if pilihan == '5':
            print ("anda keluar dari kalkulator")
            break 
        
        angka1 = float(input("masukkan angka pertama"))
        angka2 = float(input("masukkan angka kedua"))

        if  pilihan == '1':
            hasil = penjumlahan(angka1,angka2 )
            print ("hasil penjumlahan =", hasil1) 
        elif  pilihan == '2':
            hasil = pengurangan(angka1,angka2 )
            print ("hasil pengurangan =", hasil1) 
        elif  pilihan == '3':
            hasil = perkalian(angka1,angka2 )
            print ("hasil perkalian =", hasil1) 
        elif  pilihan == '4':
            hasil = pembagian(angka1,angka2 )
            print ("hasil pembagian =", hasil1) 
        else :
            print("anda tidak memasukkan pilihan")
