class Wrapper:


    def __init__(self, object):
        self.wrapped = object
        self.__x = 23

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)


class w2(Wrapper):
    pass


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    print('aaa', x.pop(2))
    print(x.wrapped)

    y = Wrapper({'а': 1, 'b': 2})
    print('bbb',list(y.keys()))
    print(y.wrapped)

    z = w2([1,2,3])
    print(z.__dict__)
