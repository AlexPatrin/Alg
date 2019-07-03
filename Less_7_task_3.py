import random

m = int(input('Введите натуральное число'))
size = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

print(f'Исходный массив: \n{array}')
# считаю количество
def medit(array):
    n = 0
    while n < len(array):
        k = 0
        for i in range(len(array)):
            if array[i] >= array[n]:
                k += 1
        # print(f'k: {k}, n: {n}')
        if k == m + 1:
            print(f'медиана {array[n]}')
        n += 1

def buble(array):
    n = 1
    while n < len(array):
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

medit(array)
print('*' * 50)
buble(array)
print(f'Отсортированный массив: \n{array}')