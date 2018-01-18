#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: ex5.py

"""
输入三个整数x,y,z，请把这三个数由小到大输出。
"""

def paixu():
    x = int(input('请输入第1个整数: '))
    y = int(input('请输入第2个整数: '))
    z = int(input('请输入第3个整数: '))

    lst = [x, y, z]
    lst.sort()
    print(lst)

paixu()
