import sys
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_out = []
print(array)

for i, item in enumerate(array):
    if item % 2 == 0:
        array_out.append(i)
print(array_out)

print('=' * 10, 'Вариант 2', '=' * 10)
mr = 0
for key in list(globals().items()):
    if '__' not in key[0] and isinstance(key[1], __builtins__.__class__) == False and key[0] != 'mr':
        mr += sys.getsizeof(key[1])
        print(f'{sys.getsizeof(key[1])}:{key}:{type(key[1])}')

print(f'Выделено памяти под переменные: {mr}')

#Выделено памяти под переменные: 220
#Windows 10 Pro. 64-разрядная ОС. Python 3.7