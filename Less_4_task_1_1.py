# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
# Вариант 1
# вариант, который был сдан в домашнем задании
import cProfile
import random

def find_max(size):
    # SIZE = 10
    MIN_ITEM = -50
    MAX_ITEM = 50
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    array_out = []
    # print(array)

    k = 1   # для определения первого вхождения
    for i, item in enumerate(array):
        if item < 0:
            if k == 1:
                max_val = item
                pos_val = i + 1
                k = 0
            else:
                if max_val < item:
                    max_val = item
                    pos_val = i + 1
    # print(f'Значение: {max_val} Позиция: {pos_val}')
    return max_val, pos_val

# print(find_max(10))
cProfile.run('find_max(10000)')

# Сложность O(n)
# Замеры скорости
#python -m timeit -n 100 -s "import Less_4_task_1_1" "Less_4_task_1_1.find_max(10)"
# 100 loops, best of 5: 28 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_1" "Less_4_task_1_1.find_max(100)"
# 100 loops, best of 5: 257 usec per loop
##python -m timeit -n 100 -s "import Less_4_task_1_1" "Less_4_task_1_1.find_max(1000)"
# 100 loops, best of 5: 2.64 msec per loop
##python -m timeit -n 100 -s "import Less_4_task_1_1" "Less_4_task_1_1.find_max(10000)"
# 100 loops, best of 5: 26.1 msec per loop

