#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: ex3.py

"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""

def wanquan():
    for i in range(1, 86):
        if 168 % i == 0:
            j = 168 / i
            if i>j and (i%2==0) and (j%2==0):
                m = (i + j)/2
                n = (i - j)/2
                x = (n**2) - 100
                print(x)

wanquan()
