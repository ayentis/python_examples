class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c = C()
c.x = 10
print(dir(c))
print(c.__dict__)
print(c.__doc__)

del(c.x)