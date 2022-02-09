class f():
    def __init__(self):
        self.__x = 1
        self.y = 2

    def func(self):
        print(self.__x, self.y, dir(self))

class z(f):
    def __init__(self):
        super().__init__()
        self.__x = 5
        self.y = 6

    def func(self):
        print(self.__x, self.y, dir(self))

e = z()
e.func()

