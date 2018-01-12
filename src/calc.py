def calc(*num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(calc(1, 2, 3, 4, 5))
print(calc(1, 2, 3, 4))
print(calc(*[1, 2, 3, 4]))
