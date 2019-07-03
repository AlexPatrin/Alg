import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: \n{array}')
# сортировка пусырьком
def buble(array):
    n = 1
    while n < len(array):
        for i in range(len(array)-1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

print('*' * 50)
buble(array)
print(f'Отсортированный массив: \n{array}')