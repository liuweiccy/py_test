def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(2))
print(power(2, 2))
print(power(4, 4))
print(power(6, 6))
print(power(8, 8))
