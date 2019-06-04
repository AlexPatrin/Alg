# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_out = []
print(array)

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
print(f'Значение: {max_val} Позиция: {pos_val}')