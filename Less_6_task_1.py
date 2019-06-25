import sys

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



print('=' * 10, 'Вариант 1', '=' * 10)
data = [SIZE, MIN_ITEM, MAX_ITEM, array, array_out, k, min_val, min_i, max_val, max_i, item, i]
print(type(data))
mr = 0
for i in data:
    mr += sys.getsizeof(i)
    print(f'{sys.getsizeof(i)} : {i}')
print(f'Выделено памяти под переменные: {mr}')

print('=' * 10, 'Вариант 2', '=' * 10)
mr = 0
for key in list(globals().items()):
    if '__' not in key[0] and isinstance(key[1], __builtins__.__class__) == False and key[0] != 'mr':
        mr += sys.getsizeof(key[1])
        print(f'{sys.getsizeof(key[1])}:{key}:{type(key[1])}')

print(f'Выделено памяти под переменные: {mr-sys.getsizeof(data)}')

#Выделено памяти под переменные: 272
#Windows 10 Pro. 64-разрядная ОС. Python 3.7
