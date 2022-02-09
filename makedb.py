from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('personsdb2')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

db = shelve.open('personsdb2')
for key in db:
    print(key, '=>', db[key])
db.close()

