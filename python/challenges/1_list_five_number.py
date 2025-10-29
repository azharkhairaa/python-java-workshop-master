# 1. Buat list berisi 5 angka
numbers = [10, 25, 7, 40, 15]
print("List awal:", numbers)

# 2. TODO: Tampilkan angka pertama dan terakhir
print("Angka pertama:")
print(numbers[0])
print("Angka terakhir:")
print(numbers[-1])

# 3. TODO: Tambahkan angka baru (apapun) ke akhir list
numbers.append(55)
print("List setelah ditambah:", numbers)

# 4. TODO: Urutkan list secara descending
numbers.sort(reverse=True)

# 5. Tampilkan hasil akhir
print("List urut descending:", numbers)