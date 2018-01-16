class Student(object):
    pass


s = Student()
s.name = "Ben"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()


# s2.set_age(25)


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(11.1)
s2.set_score(11.2)

print(s.score)
print(s2.score)


class Person(object):
    __slots__ = ('name', 'age')


p = Person()
p.age = 27
p.name = 'Eric'


# p.weigh = 90


class Students(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, (float, int)):
            raise ValueError('score must be a number')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100')
        self._score = score


s = Students()
s.score = 60
print(s.score)
