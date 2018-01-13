# -*- coding: utf-8 -*-
L = []
n = 1

while n < 99:
    L.append(n)
    n += 2

print(L)

L = ["Michael", "Sarah", "Tracy", "Bob", "Jack"]
print(L[:3])
print(L[1:3])
print(L[-1])
print(L[-2:])

L = list(range(100))
print(L)

print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[:])

T = tuple(range(100))
print(T)
print(T[:3])

S = "asdfgghjkl";
print(S)
print(S[:3])
print(S[::3])

print(ord(" "))


def trim(s):
    if len(s) == 0:
        return s
    i = 0
    e = 0
    for x in s[:]:
        if ord(x) == 32:
            i += 1
        else:
            break
    n = len(s[:])
    while n >= 0 and abs(e) < len(s):
        if ord(s[e-1]) == 32:
            e -= 1
            n -= 1
        else:
            break
    e += len(s)
    return s[i:e]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')