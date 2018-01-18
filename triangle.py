#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: triangle.py 计算三角形面积

def area_of_triangle():
	
    a = float(input('> '))
    b = float(input('> '))
    c = float(input('> '))

    s = (a + b + c)/2
    
    area = (s*(s-a)*(s-b)*(s-c))**0.5 # 海伦－秦九韶公式
    print(area)

area_of_triangle()
