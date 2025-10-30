def bucket_sort(arr):
    # Шаг 1: Проверяем наличие элементов в массиве
    if len(arr) == 0:
        return arr

    # Шаг 2: Определяем минимальное и максимальное значение массива.
    min_val = min(arr)
    max_val = max(arr)
    
    # Количество корзин выбираем исходя из диапазона значений
    num_buckets = int((max_val - min_val + 1))

    # Создаем пустые корзины
    buckets = [[] for _ in range(num_buckets)]

    # Шаг 3: Распределение элементов по корзинам
    for value in arr:
        index = int(value - min_val)
        
        # Добавляем элемент в соответствующую корзину
        buckets[index].append(value)

    # Шаг 4: Сортируем элементы внутри каждой корзины
    result = []
    for bucket in buckets:
        # Сортируем содержимое каждой корзины
        sorted_bucket = sorted(bucket)
        
        # Объединяем отсортированные корзины обратно в общий список
        result.extend(sorted_bucket)

    return result


# Пример использования:
if __name__ == "__main__":
    array_to_sort = [8, 3, 5, 1, 4, 6]
    print("Исходный массив:", array_to_sort)
    sorted_array = bucket_sort(array_to_sort)
    print("Отсортированный массив:", sorted_array)

#Исходный массив: [8, 3, 5, 1, 4, 6]
#Отсортированный массив: [1, 3, 4, 5, 6, 8]