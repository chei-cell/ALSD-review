def hitung_rata2(list_nilai):
    n = 0
    x = 0
    for i in list_nilai:
        n += i
        x += 1
        print (f"nilai ke-{x}: {i}")
    rata = n/len(list_nilai)
    return f"Rata-rata: {rata}"
        

list = [80, 75, 90, 65, 88]
print(hitung_rata2(list))
