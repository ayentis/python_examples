
# def next_bigger(n):
#     s = list(str(n))
#     for i in range(len(s)-2,-1,-1):
#         if s[i] > s[i+1]:
#             t = s[i:]
#             m = max(filter(lambda x: x<t[0], t))
#             t.remove(m)
#             t.sort(reverse=True)
#             s[i:] = [m] + t
#             return int("".join(s))
#     return -1

# def permutations(string: str):
#     def permutate(string: str, all_str: str = ""):
#         variants = []
#         for i, char in enumerate(string):
#             str_parts = string[:i]+string[i+1:]
#             full_str = all_str + char
#
#             if len(str_parts) == 0:
#                 variants.append(full_str)
#             else:
#                 variants.extend(permutate(str_parts, full_str))
#         return variants
#     rez = permutate(string)
#     return(sorted(list(set(rez))))
#
# rez = permutations("567")

# print(next_bigger(12),21)
# print(next_bigger(513),531)
# print(next_bigger(2017),2071)
# print(next_bigger(414),441)
# print(next_bigger(144),414)
# print(next_bigger(66018376008840))
# print(next_bigger(66018376001357))
# print(next_bigger(12345))

# def create_multipliers():
#     return [lambda x : i * x for i in range(5)]

# def create_multipliers():
#     multipliers = []
#
#     for i in range(5):
#         def multiplier(x):
#             return i * x
#         multipliers.append(multiplier)
#
#     return multipliers
#
# for multiplier in create_multipliers():
#     print(multiplier(2))

def centure(year: int):
    return int('0'+str(year-1)[-4:-2])+1

centure(12)
centure(412)
centure(2021)