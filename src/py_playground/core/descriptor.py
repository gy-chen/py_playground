import random


class Property():

    def __get__(self, obj, objtype):
        print('obj:', obj, 'objtype', objtype)
        return random.random()


class Container():

    p1 = Property()

if __name__ == '__main__':
    c1 = Container()
    print('c1 = Container()')
    print('print(c1.p1):', c1.p1)
    print('print(c1.p1):', c1.p1)
    p1 = c1.p1
    print('p1 = c1.p1')
    print('print(p1):', p1)
    print('print(p1):', p1)