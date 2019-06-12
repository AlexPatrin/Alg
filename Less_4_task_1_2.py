# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

# Вариант 2
import cProfile
import random

def find_max(size):
    MIN_ITEM = -50
    MAX_ITEM = 50
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    # print(array)
    array_sorted = sorted(array)
    for i, val in enumerate(array_sorted):
        if val >= 0:
            i -= 1
            max_val = array_sorted[i]
            pos_val = array.index(array_sorted[i]) + 1
            # print(f'Значение: {max_val} Позиция: {pos_val}')
            return max_val, pos_val


# print(find_max(10))
cProfile.run('find_max(10000)')

# Сложность O(n)
# Замеры скорости
#python -m timeit -n 100 -s "import Less_4_task_1_2" "Less_4_task_1_2.find_max(10)"
# 100 loops, best of 5: 28.8 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_2" "Less_4_task_1_2.find_max(100)"
# 100 loops, best of 5: 257 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_2" "Less_4_task_1_2.find_max(1000)"
# 100 loops, best of 5: 2.6 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_2" "Less_4_task_1_2.find_max(10000)"
# 100 loops, best of 5: 25.9 msec per loop
