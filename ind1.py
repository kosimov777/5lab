#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым элементом.
# Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    A = list(map(int, input("Введите список А из 10 элементов: ").split()))
    x = 0
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)
    n = 0
    for i, a in enumerate(A):
        if a > A[n]:
            n = i
    if n == 0:
        print(A)
    else:
        A[0], A[n] = A[n], A[0]
        print(A)