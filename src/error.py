import logging

try:
    print('try.....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    # logging.exception(e)
    print('except:', e)
finally:
    print('finally....')
print('End')


from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 76')
    print('99 + 88 + 76 =', r)

main()


s = '0'
n = int(s)
logging.debug('n = %d' % n)
print(10 / n)