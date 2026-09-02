# from soal1 import *

def nilai (nama, a,b,c):
    nilai_akhir = (0.3*a) + (0.3 * b) + (0.4*c)
    # na = nilai_akhir(nama, a,b,c)
    if nilai_akhir >= 85:
        print (f"Nilai {nilai_akhir}-> Grade A")
    elif nilai_akhir >= 70:
        print (f"Nilai {nilai_akhir}-> Grade B")
    elif nilai_akhir >= 60:
        print (f"Nilai {nilai_akhir}-> Grade C")
    elif nilai_akhir >= 50:
        print (f"Nilai {nilai_akhir}-> Grade D")
    else: 
        print (f"Nilai {nilai_akhir}-> Grade E")

nilai("cei", 80,90,100)