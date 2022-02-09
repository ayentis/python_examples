class SharedClass:
    spam = 99


x = SharedClass()
y = SharedClass()

print(x.spam, y.spam, SharedClass.spam)

SharedClass.spam = 88

print(x.spam, y.spam, SharedClass.spam)

y.spam = 55

print(x.spam, y.spam, SharedClass.spam)

SharedClass.spam = 77

print(x.spam, y.spam, SharedClass.spam)