#merubah ke uppercase
data = "danisyah"
data = data.upper()
print(data)

#merubah ke lowercase
nama = "DANISYAH"
nama = nama.lower()
print(nama)

#pengecekan dengan menggunakan isX method
namaDepan = "danisyah"
namaBelakang = "RIZKY"

#pengecekan lower case
apakahLower = namaDepan.islower()
print(str(apakahLower))

#pengecekan upper case
apakahUpper = namaBelakang.isupper()
print(str(apakahUpper))

#isalpha() untuk mengecek apakah semuanya huruf
apakahAlpha = namaBelakang.isalpha()
print(str(apakahAlpha))

#isalnum() untuk mengecek huruf dan angka
apakahAlnum = namaDepan.isalnum()
print(str(apakahAlnum))

#isdecimal() untuk mengecek angka
apakahDesimal = namaDepan.isdecimal()
print(str(apakahDesimal))

#isspace() untuk mengecek spasi, tab, newline \n
apakahSpace = namaDepan.isspace()
print(str(apakahSpace))

#istitle() untuk mengecek apakah dimulai dengan huruf besar
apakahTitle = namaDepan.istitle()
print(str(apakahTitle))

#ngecek komponen starswith() dan endswith()
cek_start = "Danisyah Rizky".startswith("Danisyah")
print(str(cek_start))

cek_end = "Danisyah Rizky".endswith("Rizky")
print(str(cek_end))

#penggabungan komponen join() dan split()
pisah = ["danisyah", "Rizky"]
gabung = "-".join(pisah)
print(gabung)

gabungan = "danisyahrizkyalthafangkasa"
print(gabungan.split("rizky"))

#alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("-" + kanan + "-")

kiri = "kiri".ljust(10)
print("-" + kiri + "-")

tengah = "tengah".center(20,"=")
print("-", tengah, "-")

#kebalikan strip() menghilangkan tanda "="
tengah = tengah.strip("=")
print(tengah)



