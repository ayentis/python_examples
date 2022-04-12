class A:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 2:
            raise StopIteration
        self.i += 1
        return self.i


a, b, c = A()

print(a, b, c)
