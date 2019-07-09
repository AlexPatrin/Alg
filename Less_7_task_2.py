import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив: \n{array}')

def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        # print(lefthalf, righthalf)
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1
    # print(f'merged {array}')

mergeSort(array)
print(f'Отсортированный массив: \n{array}')