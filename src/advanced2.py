from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

print(isinstance("abs", Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for v in L:
        if v > max:
            max = v
        if v < min:
            min = v
    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


L = list(range(1, 11))
print(L)

L = [x*x for x in range(1, 11)]
print(L)


L = [x*x for x in range(1, 11) if x % 2 == 0]
print(L)


L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)


import os

L = [d for d in os.listdir('.')]
print(L)


d = {'x':'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, v)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')