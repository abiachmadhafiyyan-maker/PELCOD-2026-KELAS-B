nama = input("Masukan nama anda:")
umur = input("Masukan umur anda: ")
tinggi = input("Masukan tinggi badan anda: ")
angkafavorit = int(input("Masukan angka favorit anda: "))

print ("\nData Anda:")
print ("Nama :",nama )
print ("Umur :",umur )
print ("Tinggi :",tinggi )
print ("Angka favorit :",angkafavorit)

pensil = 2000
buku = 5000

print(f"harga pensil RP.{pensil} per buah")
print(f"harga buku RP.{buku} per buah")

print("4 harga pensil = RP.",pensil *4 )
print("2 harga buku = RP.",buku *2 )

totalBelanja = pensil*4 + buku*2
print(f"total belanja {totalBelanja}")

if angkafavorit % 2 == 0:
    print("Angka favorit adalah genap")
else:
    print("Angka favorit adalah ganjil")
