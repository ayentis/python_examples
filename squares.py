class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


class SquaresYield:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for x in range(self.start, self.stop + 1):
            yield x ** 2

x = list(i for i in SquaresYield(1,5))
print(x)