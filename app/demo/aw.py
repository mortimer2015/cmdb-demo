# -*- coding: UTF-8 -*-
__author__ = 'hunter'


# -*- coding: UTF-8 -*-
__author__ = 'hunter'


def ac(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print("acccc")
        return func(*args, **kwargs)
    return wrapper


def cc(message='accc'):
    print(message)
    def ac(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):

            return func(*args, **kwargs)
        return wrapper
    return ac


@cc()
def a():
    # bia.b()
    print('a')


if __name__ == '__main__':
    # a()
    print('2333')



