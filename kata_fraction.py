import numpy as np
# import math
# import functools
#
# a = [[1, 2], [1, 3], [1, 4]]
# b = [[6, 12], [4, 12], [3, 12]]
#
# def f(a,b):
#     rez = abs(a * b) // math.gcd(a, b)
#     print(rez)
#     return rez
#
#
# def convert_fracts(lst):
#     # lcm = np.lcm.reduce([val[1] for val in lst])
#     # return [ [int(val[0]*lcm/val[1]), lcm] for val in lst]
#
#     lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
#     tmp_list = list(map(lambda x : x[1] ,list(lst)))
#     # print(tmp_list)
#     lcm_num = functools.reduce(f,tmp_list)
#     # print(lcm_num)
#
# print(convert_fracts(a))

# a = 18
# b = 30
#
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# print(a + b)
# mult = 2
# lst = range(6)
#
# map_rez = map(lambda x: x**mult,[1,6,9])
#
# mult = 2
# lst = [1,2,3,6,9]
#
# # print(*[j for j in map_rez])
#
# for j in map_rez:
#     print(j)

class B:
    def __init__(self):
        print('В.__init__')
        super().__init__()

class C:
    def __init__(self):
        print('C.__init__')
        super().__init__()

class D(B,C):
    def __init__(self):
        print('D.__init__')
        B.__init__(self)
        C.__init__(self)


x = D()

