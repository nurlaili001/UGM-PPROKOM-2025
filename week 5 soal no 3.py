n = int(input("Masukkan jumlah nilai: "))
total = 0
for i in range(n):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    total += nilai

rata_rata = total / n
print(f"Rata-rata dari {n} nilai: {rata_rata}")