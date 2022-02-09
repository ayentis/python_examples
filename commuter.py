class Commuter1:
    def __init__ (self, val):
        self.val = val
    def __add__ (self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__ (self, other):
        return other + self.val


class Commuter2:
    def __init__ (self, val):
        self.val = val
    def __add__ (self, other):
        print('add', self.val, other)
        return self.val + other
    def __radd__ (self, other):
        return self.__add__(other)


class Commuter3:
    def __init__ (self, val):
        self.val = val
    def __add__ (self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self + other


class Commuter4:
    def __init__ (self, val):
        self.val = val
    def __add__ (self, other):
        print('add', self.val, other)
        return self.val + other
    __radd__ = __add__


class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__ (self, other):
        return self.data < other

X = C()
print(X > 'ham')
print('ham' > X)
print(X < 'ham')

# x = Commuter4(88)
# y = Commuter4(99)
#
# z = x+1
# z = y+1
# z = x+y
#
# print(z)