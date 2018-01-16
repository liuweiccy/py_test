L = list(map(lambda x:x*x, [1,2,3,4]))
print(L)

f = lambda x, y : x + y
print(f(2,3))
print(f)


def build(x, y):
    return lambda: x * y


print(build(2,3)())


L = list(filter(lambda n : n % 2 == 1, range(1, 20)))

print(L)

f = build
f1 = build(2, 3)
print(build.__name__)
print(f.__name__)
print(f1.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text):
    def text1(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s:" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return text1

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log1("执行")
def now():
    print("2017-1-15")


print(now())

f = log(now)
print(f.__name__)

import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        s = time.time()
        value = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - s))
        return value
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


print(int('1234', 8))
print(int('1234', 16))


int2 = functools.partial(int, base=2)

print(int2("1100"))
