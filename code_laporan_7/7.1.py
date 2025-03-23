
n = int(input("Masukkan bilangan n: "))
def bilprima(bilangan): 
    if bilangan < 2:#untk Memeriksa kalau bil kurang dari 2
        return False
    for i in range(2, int(bilangan**0.5) + 1):#perulangan untk memeriksa semua bilangan dari 2 hingga bilangan - 1
        if bilangan % i == 0:# memeriksa apakah bilangan habis dibagi oleh i (yaitu, bilangan % i == 0)
            return False
    return True

def bilprima_terdekat(n):#mencari bilangan prima terbesar yang kurang dari n
    for i in range(n - 1, 1, -1):#dari n - 1 dan mengecek mundur hingga 2
        if bilprima(i):#memeriksa apakah i adalah bilangan prima.
            return i
    return None


billprima_terdekat = bilprima_terdekat(n)#menyimpan hasil dari fungsi tersebut untuk digunakan dalam percabangan 

if billprima_terdekat:# UNTUK menampilkan hasil hanya jika bilangan prima terdekat 
    print(f" maka prima terdekat {n} adalah {billprima_terdekat}.")
else:
    print(f"kosong {n}.")


