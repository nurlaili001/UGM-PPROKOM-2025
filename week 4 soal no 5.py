nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai ujian: "))
if nilai >= 70:
    status = "lulus"
else:
    status = "tidak lulus"
print(f"Siswa atas nama {nama} dinyatakan {status}.")