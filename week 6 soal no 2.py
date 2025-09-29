nilai = set({3,6,9,2,5,7})
nilai.update({1,4,8,10})
print("Nilai setelah penambahan: ", nilai)

elemen_hapus = {1, 3, 4, 5, 7, 8, 10}
for elemen in elemen_hapus:
    if elemen in nilai: 
        nilai.remove(elemen)
print("Nilai setelah penghapusan: ", nilai)