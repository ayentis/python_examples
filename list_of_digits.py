def add_one(l: list) -> list:
     # return lambda l: list(map(int, list(str(int(''.join(map(str, l))) + 1))))
     return [int(x) for x in str(int(''.join(map(str,l))) + 1)]


print(add_one([0]))
print(add_one([1,2,3,4]))
print(add_one([9,9,9,9,9]))
print(add_one([9]))

