
def find_outlier(l:list):
    x = list(map(lambda x: x % 2, l))
    y = list(enumerate(x))

    y.sort(key=lambda z: x.count(z[1]))

    return l[y[0][0]]



print(find_outlier([2, 4, 0, 4, 11, 36])) #-> 11
print(find_outlier([160, 3, 19, 11, -21])) #-> 160
print(find_outlier([-1, 1, 3, 3, 2, -11, -21])) #-> 2
