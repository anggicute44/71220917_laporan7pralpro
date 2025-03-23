# nilai = int(input("Masukkan nilai ujian: "))

# # Kondisi 1: Nilai ≥ 80
# if nilai >= 80:
#     print("bagus bgt")
    
   
#     if nilai >= 90:
#         print("hebat bgt")
#     else:
#         print("pertahankan lagi")

# # Kondisi 2: Nilai 60 - 79
# else:
#     if nilai >= 60:
#         print("Cukup ")
#         print("ayo tingkatkan")
    
#     # Kondisi 3: Nilai < 60
#     else:
#         print("Kurang bgt")
        
        
#         if nilai < 40:
#             print("otw gak lulus")
#             print("Segera belajar")
#         else:
#             print("Jangan menyerah")

# umurku = 20
# if umurku >= 20:
#     print("aku sudah dewasa.")


# umurku = 11
# if umurku >= 18:
#     print("aku sudah dewasa.")
# else:
#     print("aku masih di kecil.")

umurku = int(input("Masukkan umur kamu: "))

if umurku < 0:
    print("masih bayi")
elif umurku < 13:
    print("Aku masih anak-anak")
elif umurku < 20:
    print("aku remaja")
elif umurku < 60:
    print("aku udh dewasa")
else:
    print("aku udh tua")