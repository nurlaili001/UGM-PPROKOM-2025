set_A = {20, 30, 40, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C = {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}
Irisan_set_A_C_D = set_A & set_C & set_D 
Gabungan_set_A_B = set_A | set_B
Selisih_gabungan_set_D = Gabungan_set_A_B - set_D
Selisih_simetris_set_B_C = set_B ^ set_C
Gabungan_set_C_D = set_C | set_D
Irisan_gabungan_set_AB_CD = Gabungan_set_A_B & Gabungan_set_C_D
print("Irisan set_A, set_C, dan set_D: ", Irisan_set_A_C_D)
print("Gabungan set_A dan set_B, lalu selisih dengan set_D: ", Selisih_gabungan_set_D)
print("Selisih simetris set_B dan set_C: ", Selisih_simetris_set_B_C)
print("Gabungan set_A, B dan set_C,D, lalu irisan kedua gabungan: ", Irisan_gabungan_set_AB_CD)