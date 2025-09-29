buah_buahan = {
    "apel": 15000,
    "jeruk": 10000,
    "anggur": 25000
}

print("Harga Jeruk: Rp", buah_buahan["jeruk"])
print()

buah_buahan["mangga"] = 12000
print("Dictionary buah_buahan terbaru: ")
print("1. Setelah Penambahan Buah Mangga") 
print(buah_buahan)

buah_buahan["anggur"] = 20000
print("2. Setelah Memperbarui Harga Anggur")
print(buah_buahan)

del buah_buahan["jeruk"]
print("3. Setelah Menghapus Buah Jeruk")
print(buah_buahan)