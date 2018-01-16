L = [36, 5, -12, 9, -21]

print(sorted(L))

print(sorted(L, key=abs))
print(sorted(L, key=abs, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))


def by_score(n):
    return n[1]


print(sorted(L, key= by_score, reverse= True))

