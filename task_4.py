# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо


num_number = int(input('Сколько чисел будем вводить?'))
num_cifra = int(input('Какую цифру будем искать?'))
k = 0
while num_number > 0:
    number = input('Введите число')
    for i in number:
        if int(i) == num_cifra:
            k += 1
    num_number -= 1
print(f'Всего "{num_cifra}" всречается {k} раз')
