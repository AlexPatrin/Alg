# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# prime = int(input('Введите номер простого числа'))

# import cProfile


def CheckPrime(current_pos, prime, count_prime):
    for i in range(2, current_pos+1):
        if current_pos % i == 0 and current_pos != i:
            return count_prime
        elif current_pos % i == 0 and current_pos == i:
            count_prime += 1
            # if count_prime == prime:
                # print(current_pos)
                # exit()
            return count_prime

def mine(prime):
    # prime = 3
    count_prime = 0
    current_pos = 1
    while True:
        current_pos += 1
        count_prime = CheckPrime(current_pos, prime, count_prime)
        if count_prime == prime:
            # print(current_pos)
            # count_prime += 1
            return current_pos


# print(mine(500))
# cProfile.run('mine(500)')

# Сложность алгоритма
# O(n**2)
#
# Замеры скорости
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(5)"
# 100 loops, best of 5: 12.5 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(50)"
# 100 loops, best of 5: 988 usec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(100)"
# 100 loops, best of 5: 4.51 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(200)"
# 100 loops, best of 5: 21.7 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(300)"
# 100 loops, best of 5: 55.2 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(400)"
# 100 loops, best of 5: 107 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(500)"
# 100 loops, best of 5: 168 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_2" "Less_4_task_2_2.mine(600)"
# 100 loops, best of 5: 260 msec per loop
