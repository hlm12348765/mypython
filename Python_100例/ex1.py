#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: ex1.py

"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

def sanweishu():
    list = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    s1 = str(i) + str(j) + str(k)
                    s2 = ''.join(s1)
                    list.append(s2)
                else:
                    pass
    print("能组成{}个互不相同且无重复数字的三位数".format(len(list)))
    print("各是: {}".format(list))

sanweishu()
