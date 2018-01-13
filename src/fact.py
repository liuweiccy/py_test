def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(1))
print(fact(10))
print(fact(100))


def fact1(n):
    return fact_itr(n, 1)


def fact_itr(n, v):
    if n == 1:
        return v
    else:
        return fact_itr(n - 1, n * v)


print(fact1(1))
print(fact1(10))
print(fact1(100))
print(fact1(900))
