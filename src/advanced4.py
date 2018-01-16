from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((), Iterable))
print(isinstance(100, Iterable))


print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))


print(isinstance(iter([]), Iterator))