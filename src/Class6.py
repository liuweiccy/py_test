class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name


print(Student('Eric'))
s = Student("Amy")


class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 10000:
            raise StopIteration()
        return self.__a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


for a in Fib():
    print(a)

print(Fib()[5])
print(Fib()[15])
print(Fib()[115])


class Student2(object):
    def __init__(self):
        self.name = 'Eric'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda : 30
        raise AttributeError("%s no attr" % item)

s = Student2()
print(s.name)
print(s.score)
print(s.age())
# print(s.height)



class Chain(object):
    def __init__(self, path = ''):
        self.__path = path

    def __str__(self):
        return self.__path

    def __getattr__(self, item):
        return Chain("%s/%s" % (self.__path, item))

    def __call__(self, *args, **kwargs):
        return 'My name is %s' % args[0]

print(Chain().status.user.timeline.list)


def max3(L):
    pass

c = Chain("api/name")
print(c("interface"))

print(callable(Student))
print(callable(max))
print(callable(Chain))
print(callable(''))
print(callable(max3))