
n = int(input("Masukkan nilai n: "))
def htngfaktor(bilangan):
    if bilangan == 0 or bilangan == 1: #mengecek apakah nilai bilangan adalah 0 atau 1
        return 1 # Faktorial dari 0 atau 1 adalah 1
    faktorial = 1 #menyimpan hasil perkalian faktorial
    for i in range(2, bilangan + 1):
        faktorial *= i  # Kalikan nilai faktorial dengan i
    return faktorial

def output_deret(n):
    for i in range(n, 0, -1):
        faktorial = htngfaktor(i)
        print(faktorial, end=" ")  # Cetak faktorial
        for j in range(i, 0, -1):  # Cetak deret angka
            print(j, end=" ")
        print()  # Pindah ke baris baru setelah selesai mencetak satu baris

output_deret(n)

