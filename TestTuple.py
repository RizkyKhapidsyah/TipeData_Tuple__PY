import sys

data_list = [1, 2, 3, 4, 5, "Sepeda", "Mobil", False, 3.14]
data_tuple = (1, 2, 3, 4, 5, "Sepeda", "Mobil", False, 3.14)

besar_data_List = sys.getsizeof(data_list)
besar_data_Tuple = sys.getsizeof(data_tuple)

print("Besar Data List:", besar_data_List)
print("Besar Data List:", besar_data_Tuple)

