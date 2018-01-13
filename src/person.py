def person(name, age, *, city, job):
    print("name:", name, "age:", age, city, job)


person("PY", 30, city="Beijing", job="Coder")


def person1(name, age, *args, city, job):
    print(name, age, args, city, job)


person1("PY", 30, 1, 2, 3, 4, [2, 2], city="Beijing", job="Coder")


def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person2("Erlang", 35, job="SSS")


def f1(a, b, c=0, *args, **kw):
    print(a, b, c, args, kw)


def f2(a, b, c=0, *, d, **kw):
    print(a, b, c, d, kw)


f1(1, 2, 4, 3, 3, 3, city="Beijing", job="coder")
f2(1, 2, 4, d="name", a1=1, b1=2, c1=3, e=4)


def product(*x):
    if len(x) == 0:
        raise TypeError("args error")
    value = 1
    for v in x:
        value *= v
    return value


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
