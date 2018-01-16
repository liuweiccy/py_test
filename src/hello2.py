'a test module'

__author__ = 'VV'

import sys

def _test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello, %s!" % args[1])
    else:
        print("太多参数")

def test2():
    _test()


if __name__ == '__main__':
    test2()