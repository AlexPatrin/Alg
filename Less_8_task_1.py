"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""

import hashlib

def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return h_subs

def count_hash(s):
    sub_frame = []
    for i in range(len(s)+1):
        for j in range(len(s)+1):
            if s[i:j] != '' and s[i:j] != s:
                # print(f'{i}:{j} - {s[i:j]}')
                sub_frame.append(rabin_karp(s, s[i:j]))
    sub_frame = list(set(sub_frame))
    return len(sub_frame)

print(count_hash('abrakadabra'))
print(count_hash('sova'))
print(count_hash('papa'))