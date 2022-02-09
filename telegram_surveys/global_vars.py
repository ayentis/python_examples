var = 1
def x():
    var = 2
    def y():
        global var
        var = 3
    y()

x()
print(var)

