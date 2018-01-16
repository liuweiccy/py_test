# -*- coding: utf-8 -*-

import hello2
import sys

name = input("输入你的名字：")
print("hello, ", name)
print('''
    liuwei
    ccy
    hahah
''')

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


hello2.test2()


print(sys.path)