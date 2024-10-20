numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
lengh = len(numbers)
k = numbers.index(None)

sr_arif = (sum(numbers[:k])+sum(numbers[(k+1):]))/lengh

numbers[4] = sr_arif
print("Измененный список:", numbers)
