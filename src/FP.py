import math

print(abs(-10))
print(abs)


def add(a, b, f):
    return f(a) + f(b)


print(add(-1, 2, abs))


def f(x):
    return x * x


r = map(f, [x for x in range(10)])
print(list(r))

r1 = map(str, [x for x in range(10)])
print(list(r1))

from functools import reduce


def add1(x, y):
    return x + y


print(reduce(add1, [1, 2, 3, 4, 5], 5))


def fn(x, y):
    return 10 * x + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


num = reduce(fn, map(char2num, "13569"))
print(num)


def normalize(name):
    if len(name) == 1:
        return str.upper(name)
    name1 = str.lower(name)
    name2 = str.upper(name[:1]) + name1[1:]
    return name2


# 测试:
L1 = ['adam', 'LISA', 'barT', 'A', ""]
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L, 1)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    array = s.split(".")
    return reduce(fn, map(char2num, array[0])) + reduce(fn, map(char2num, array[1])) * math.pow(10, -len(array[1]))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 10, 5, 6, 11, 7, 8, 9])))


def not_empty(s):
    return s and s.strip()


L = list(filter(not_empty, ['A', '   ', ' bc   ']))
print(L)


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 10:
        print(n)
    else:
        break


def is_palindrome(n):
    s = str(n)
    if len(s) == 1:
        return True
    if len(s) % 2 == 0:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:]
        for i in range(0, len(s1)):
            if s1[i] == s2[-(i+1)]:
                pass
            else:
                return False
        return True
    else:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2 + 1:]
        for i in range(0, len(s1)):
            if s1[i] == s2[-(i+1)]:
                pass
            else:
                return False
        return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

