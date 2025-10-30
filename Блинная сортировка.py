def flip(arr, k):
    # Перевернем первые k+1 элементов массива arr
    arr[:k + 1] = reversed(arr[:k + 1])

def find_max_index(arr, n):
    # Найдем индекс максимального элемента среди первых n элементов массива
    max_idx = 0
    for i in range(n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    curr_size = len(arr)
    
    while curr_size > 1:
        # Шаг 1: находим индекс максимального элемента среди всех неотсортированных элементов
        max_idx = find_max_index(arr, curr_size)
        
        # Если максимум уже находится на своем месте, переходим к следующему шагу
        if max_idx != curr_size - 1:
            # Шаг 2: перевернём массив таким образом
            flip(arr, max_idx)
            
            # Шаг 3: теперь перевернём весь текущий отсортированный сегмент
            flip(arr, curr_size - 1)
        
        # Уменьшаем размер обрабатываемого сегмента
        curr_size -= 1
    
    return arr

# Пример использования
arr = [3, 6, 2, 4, 5]
sorted_arr = pancake_sort(arr)
print("Отсортированный массив:", sorted_arr)

#Отсортированный массив: [2, 3, 4, 5, 6]