# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

# Вариант 3
# import cProfile
import random

def find_max(size):
    MIN_ITEM = -50
    MAX_ITEM = 50
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    # print(array)
    num = float('-inf')
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i + 1
    if num != float('-inf'):
        # print(f'val {num} index {index}')
        return num, index

# print(find_max(10))
# cProfile.run('find_max(10000)')

# Сложность O(n)
# Замеры скорости
#python -m timeit -n 100 -s "import Less_4_task_1_3" "Less_4_task_1_3.find_max(10)"
# 100 loops, best of 5: 31.6 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_3" "Less_4_task_1_3.find_max(100)"
# 100 loops, best of 5: 273 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_3" "Less_4_task_1_3.find_max(1000)"
# 100 loops, best of 5: 2.58 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_1_3" "Less_4_task_1_3.find_max(10000)"
# 100 loops, best of 5: 25.6 msec per loop
