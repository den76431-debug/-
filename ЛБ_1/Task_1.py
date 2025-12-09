numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_missing_item = numbers.index(None)
sum_of_numbers = sum(num for num in numbers if num is not None)
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
numbers[index_missing_item] = average_of_numbers
print("Измененный список:", numbers)
