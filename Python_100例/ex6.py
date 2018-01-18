#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: ex6.py

"""
斐波那契数列
"""

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))

def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    fibonacci = [1, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

print(fibonacci(10))
