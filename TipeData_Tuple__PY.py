# List
Ganjil = [1, 3, 5, 7, 9]

# Tuple
Genap = (2, 4, 6, 8, 8, 10)

print("Data Pada Array: Ganjil, adalah berjenis : ", type(Ganjil))
print("Data Pada Array: Genap, adalah berjenis  : ", type(Genap), '\n')

print(dir(Ganjil), '\n')
print(dir(Genap), '\n')

Ganjil.append(3)
Ganjil[2] = 63 # Tipe: List Data Dapat Dirubah
print(Ganjil)

print("Jumlah Angka '8' Pada Data: Genap, adalah sebanyak:", Genap.count(8), "buah data")
print("Angka '6' berada pada Index Ke:", Genap.index(6))
