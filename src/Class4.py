from src import Class3
import types


print(type(123))
print(type(''))
print(type(None))
print(type(abs))
print(type(Class3.Dog))
print(type(Class3.Dog.run))
print(type(Class3.run_twice) == types.FunctionType)
print(type(123) == int)

print(dir(""))