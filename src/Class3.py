class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):

    def run(self):
        print('Dog is running')


class Cat(Animal):

    def run(self):
        print('Cat is running')


dog = Dog()
cat = Cat()

dog.run()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())

