# python code to demonstrate working of reduce()

# importing functools for reduce()
from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2, ]


# def ex(a,b):
#     print(a,b)
#     return(a+b)
#
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# # print(functools.reduce(lambda a, b: a + b, lis))
# print(functools.reduce(ex, lis))
#
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

def fun(acc, x):
    print(acc, x)
    # return x + acc[::-1] + x
    acc.append(x)
    return acc

vals = (chr(x) for x in range(ord('a'), ord('d')))
# print(reduce(lambda acc, x: x + acc[::-1] + x, vals, ''))
print(reduce(fun, vals, []))