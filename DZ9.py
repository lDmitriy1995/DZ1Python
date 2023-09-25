def bubble_sort_advanced(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1  # Уменьшаем длину списка на каждой итерации
    return arr

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort_advanced(my_list)
print("Отсортированный список:", sorted_list)
