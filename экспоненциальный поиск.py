def binary_search(arr, left, right, target):
    # Бинарный поиск между левым и правым границами массива arr
    while left <= right:
        mid = (left + right) // 2   # Вычисляем средний индекс

        if arr[mid] == target:       # Если нашли нужный элемент
            return mid               # Возвращаем его позицию
        
        elif arr[mid] < target:      # Если цель справа от середины
            left = mid + 1           # Уменьшаем левую границу
            
        else:                        # Иначе цель слева от середины
            right = mid - 1          # Увеличиваем правую границу
    
    return -1                       # Элемент не найден


def exponential_search(arr, target):
    n = len(arr)
    
    # Проверяем первый элемент отдельно
    if arr[0] == target:
        return 0                     # Возврат первой позиции, если совпадение сразу найдено
    
    i = 1                           # Начнем проверку с второго элемента
    
    # Экспоненциально увеличиваем границы поиска
    while i < n and arr[i] <= target:
        i *= 2                      # Удвоение текущего индекса (быстро перемещаемся вперед)
    
    # После выхода из цикла ищем элемент методом бинарного поиска
    return binary_search(arr, i//2, min(i, n-1), target)


# Пример использования
if __name__ == "__main__":
    sorted_array = [1, 3, 5, 8, 10, 12, 15]
    x = 10                          # Искомое число
    result = exponential_search(sorted_array, x)

    if result != -1:
        print(f'Элемент {x} находится на позиции {result}')
    else:
        print('Элемент не найден')

#Пример вывода
#Элемент 10 находится на позиции 4