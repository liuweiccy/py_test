L = [x * x for x in range(10)]
print(L)

G = (x * x for x in range(10))
print(G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return "Done"


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "Done"

f = fib1(10)
print(f)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()

for _ in o:
    pass


for v in fib1(10):
    print(v)

f = fib1(10)
while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print(e.value)
        break







