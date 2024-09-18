# cuaca = "mendung"

# if cuaca == "mendung":
#     print("diam dirumah")
# else : 
#     print("hari ini mendung")




# Umur = int(input("Masukkan umur anda : "))
# if Umur > 0 :
#     if Umur <= 10:
#         print( "Umur anda kategori anak anak")
#     elif Umur <= 18:
#         print("Umur anda termasuk kategori remaja")
#     elif Umur <= 21:
#         print("Umur anda termasuk kategori dewasa")
#     elif Umur <= 35:
#         print("Umur anda termasuk kategori paruh baya")
#     else :
#         print("Umur anda termasuk kategori tua")
# else : 
#     print("input Umur harus bilangan positif")




# NIM = int(input("Masukkan nim"))

# if NIM  >= 1 and NIM <= 50 :
#     if NIM >= 1 and NIM <= 25 :
#         print("kelas A'1")
#     else : 
#         print("kelas A'2")
# elif NIM >= 51 and NIM <= 100 :
#     if NIM >= 51 and NIM <= 75 :
#         print("kelas B'1")
#     else : 
#         print("kelas B'2")
# elif NIM >= 101 and NIM <= 121 :
#     if NIM >= 101 and NIM <= 110 :
#         print("kelas C'1")
#     else : 
#         print("kelas C'2")
# else : 
#     print("Anda bukan mahasiswa Informatika")







nim = int(input("masukkan nim : "))
hasil = "kelas A" if nim >= 1 and nim <= 50 else "kelas B" if nim >= 51 and nim <= 75 else "kelas C" if nim >= 76 and nim <= 121 else "manusia siluman"
print(hasil) 
print(type(hasil))

