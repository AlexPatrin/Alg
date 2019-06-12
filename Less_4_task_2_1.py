# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

# import cProfile

def sieve_eratos(n, count_pos, prime):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    if len(res) < prime:
        n = n ** 2
        return n, False
    return res[prime-1], True

def mine(prime):
    count_pos = 0
    n = 1000
    while True:
        check = sieve_eratos(n, count_pos, prime)
        if check[1] == True:
            val = check[0]
            return val
        elif check[1] == False:
            n = n * 10
# print(mine(500))
# cProfile.run('mine(500)')
#
# Сложность алгоритма
# O(n log(log n)) до n^5
# Если определять по пройденному материалу, то O (n * log n)

# Замеры скорости при n = n * 10. Если, например n = n ** 2, то я не дождался завершения 100 тестов при поиске 200-го числа
#python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(5)"
# 100 loops, best of 5: 540 usec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(50)"
# 100 loops, best of 5: 523 usec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(100)"
# 100 loops, best of 5: 522 usec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(200)"
# 100 loops, best of 5: 6.1 msec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(300)"
# 100 loops, best of 5: 6.58 msec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(400)"
# 100 loops, best of 5: 6.14 msec per loop
##python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(500)"
# 100 loops, best of 5: 6.06 msec per loop
#python -m timeit -n 100 -s "import Less_4_task_2_1" "Less_4_task_2_1.mine(5000)"
# 100 loops, best of 5: 72.8 msec per loop

