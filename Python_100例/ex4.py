#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Nie Bowen
# Filename: ex4.py

"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

def judge_day():
    year = int(input('输入年份: '))
    month = int(input('输入月份: '))
    day = int(input('输入日期: '))
    dict_l = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dict_c = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    sum_day = 0

    if month == 1:
        days_num = day
        print("{}年{}月{}日是这一年的第{}天".format(year, month, day, days_num))
    else:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print("{}是闰年".format(year))
            if day < 0 or month < 0 or month > 12 or day > dict_l[month]:
                print("无效日期: {}年{}月{}日".format(year, month, day))
            else:
                for i in range(1, month):
                    sum_day += dict_l[i]
                    days_num = sum_day + day
                print("{}年{}月{}日是这一年的第{}天".format(year, month, day, days_num))
        else:
            print("{}是平年".format(year))
            if day < 0 or month < 0 or month > 12 or day > dict_c[month]:
                print("无效日期: {}年{}月{}日".format(year, month, day))
            else:
                for i in range(1, month):
                    sum_day += dict_c[i]
                    days_num = sum_day + day
                print("{}年{}月{}日是这一年的第{}天".format(year, month, day, days_num))

judge_day()
