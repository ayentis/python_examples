
from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay = int(self.pay*(1+percent))

    # def __repr__(self):
    #     return '[Person: %s %s]' % (self.name, self.pay)

    # def __str__(self):
    #     return '[Person str: %s %s]' % (self.name, self.pay)


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.1):
        Person.giveRaise(self, percent + bonus)

# class Manager:
#     def __init__(self, name, pay):
#         self.person = Person(name, 'mgr', pay)
#
#     def giveRaise(self, percent, bonus=.1):
#         self.person.giveRaise(percent + bonus)

    # def __getattr__(self, attr):
    #     return getattr(self.person, attr)
    #
    # def __repr__(self):
    #     return str(self.person)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'dev', 100000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.1)
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

    # print('--Dep—')
    # development = Department(bob, sue)  # Внедрить объекты в составной объект
    # development.addMember(tom)
    # development.giveRaises(.10)
    # development.showAll()

    # print('--All three—')
    # for obj in (bob, sue, tom):
    #     obj.giveRaise(.10)
    #     print(obj)

