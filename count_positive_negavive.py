from functools import reduce

def do(x,y):
    if y > 0:
        x[0]+=1
    elif y < 0:
        x[1] += 1
    return x

def count(list_d):
    # return reduce(do,in_l,[0,0])
    return len((list(filter(lambda x:x>0, list_d)))), len((list(filter(lambda x:x<0, list_d))))



print(count([5, 4, 1, 2, -1, -2])) #-> (4, 2)
print(count([1, 0, -1])) #-> (1, 1)
print(count([0, 0, 0, 0])) #-> (0, 0)