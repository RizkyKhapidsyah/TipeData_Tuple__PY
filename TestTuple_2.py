import timeit

data_list = timeit.timeit(stmt="[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=1000000)
data_tuple = timeit.timeit(stmt="(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=1000000)

print("Waktu Untuk Memproses List:", data_list)
print("Waktu Untuk Memproses List:", data_tuple)