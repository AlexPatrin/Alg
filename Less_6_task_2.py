import sys
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
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
if max_i > min_i:
    pos_i_max = max_i
    pos_i_min = min_i
else:
    pos_i_max = min_i
    pos_i_min = max_i
# count_pos = abs(max_i - min_i) - 1
print(f'min_val: {min_val}, max_val: {max_val}, pos_min: {pos_i_min}, pos_max: {pos_i_max}')

summa = 0
if pos_i_max - pos_i_min - 1 > 0:
    for j in range(pos_i_min + 1, pos_i_max):
        summa = summa + array[j]
else:
    print('Сумму посчитать невозможно')
    exit()
print(f'Сумма между элементами: {summa}')

print('=' * 10, 'Вариант 2', '=' * 10)
mr = 0
for key in list(globals().items()):
    if '__' not in key[0] and isinstance(key[1], __builtins__.__class__) == False and key[0] != 'mr':
        mr += sys.getsizeof(key[1])
        print(f'{sys.getsizeof(key[1])}:{key}:{type(key[1])}')

print(f'Выделено памяти под переменные: {mr}')

#Выделено памяти под переменные: 330
#Windows 10 Pro. 64-разрядная ОС. Python 3.7