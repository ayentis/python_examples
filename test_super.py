class Employee:
    def __init__(self, name, salary):
        print('init.Employee')
        self.name = name
        self.salary = salary


class Chef1(Employee):
    def __init__(self, name):
        print('init.Chef1')
        Employee.__init__(self, name, 50000)


class Server1(Employee):
    def __init__(self, name):
        print('init.Server1')
        Employee.__init__(self, name, 40000)


class Chef2(Employee):
    def __init__(self, name):
        print('init.Chef2')
        super().__init__(name, 50000)


class Server2(Employee):
    def __init__(self, name):
        print('init.Server2')
        super().__init__(name, 40000)


class TwoJobs(Chef2, Server2):
    pass


# bob = Chef2('Bob')
# sue = Server2('Sue')
# print(bob.salary, sue.salary)

print(TwoJobs.__mro__)
tom = TwoJobs('Tom')

