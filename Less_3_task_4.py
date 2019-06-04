# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_out = []
print(array)

k = 1   # для определения первого вхождения
for i, item in enumerate(array):
    if k == 1:
        k = 0
        min_val = item
        min_i = i
        max_val = item
        max_i = i
    else:
        if max_val < item:
            max_val = item
            max_i = i
        if min_val > item:
            min_val = item
            min_i = i
print(f'min_val: {min_val}, max_val: {max_val}, min_ind: {min_i}, max_ind: {max_i}')
array[min_i] = max_val
array[max_i] = min_val
print(array)