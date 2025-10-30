def bead_sort(lst):
    # Шаг 1: Подготовка матрицы бусинок
    max_value = max(lst)
    
    # Создаем массив нулей размером len(lst) x max_value,
    beads_matrix = [[1 if j < lst[i] else 0 for j in range(max_value)] for i in range(len(lst))]

    # Пример вывода промежуточной матрицы перед сортировкой
    print("Исходная матрица:")
    for row in beads_matrix:
        print(row)

    # Шаг 2: Гравитация (перераспределение бусинок)
    for col_idx in range(max_value):
        count = sum(beads_matrix[row][col_idx] for row in range(len(lst)))  # считаем количество единиц в данном столбце

        # Заполняем столбец снизу вверх единицами
        for row in range(count):
            beads_matrix[row][col_idx] = 1
        
        # Остальное пространство заполняем нулями
        for row in range(count, len(lst)):
            beads_matrix[row][col_idx] = 0

    # Пример вывода промежуточной матрицы после перераспределения
    print("\nМатрица после гравитации:")
    for row in beads_matrix:
        print(row)

    # Шаг 3: Преобразование обратно в список целых чисел
    sorted_list = []
    for row in beads_matrix:
        num_ones = sum(row)  # подсчитываем число единиц в строке
        sorted_list.append(num_ones)

    return sorted_list


# Пример использования
if __name__ == "__main__":
    numbers = [5, 3, 1, 8]
    result = bead_sort(numbers)
    print(f"\nОтсортированный список: {result}")

#Исходная матрица:
#[1, 1, 1, 1, 1, 0, 0, 0]
#[1, 1, 1, 0, 0, 0, 0, 0]
#[1, 0, 0, 0, 0, 0, 0, 0]
#[1, 1, 1, 1, 1, 1, 1, 1]

#Матрица после гравитации:
#[1, 1, 1, 1, 1, 1, 1, 1]
#[1, 1, 1, 1, 1, 0, 0, 0]
#[1, 1, 1, 0, 0, 0, 0, 0]
#[1, 0, 0, 0, 0, 0, 0, 0]

#Отсортированный список: [8, 5, 3, 1]