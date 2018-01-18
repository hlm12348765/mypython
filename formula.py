#!/usr/bin/env python3
# -*- coding; utf-8 -*-
# Author: Nie Bowen
# Filename: formula.py 求解一元二次方程

def formula():
    a = float(input('input a: '))
    b = float(input('input b: '))
    c = float(input('input c: '))

    delta = b**2 - 4*a*c

    print("方程为: {}x^2 + {}x + {} = 0".format(a, b, c))

    if a == 0:
        print("这是一次方程")
    else:
        if delta > 0:
            x1 = (-b - delta**0.5)/(2*a)
            x2 = (-b + delta**0.5)/(2*a)
            print("方程有2个不相等的实根{}和{}".format(x1, x2))
        elif delta == 0:
            x1 = x2 = (-b)/(2*a)
            print("方程有2个相等的实根{}".format(x1))
        else:
            print("方程没有实根")

formula()
