
def to_one_dimension_list(a):
    rez = []
    for el in a:
        if isinstance(el, list):
            rez.extend(to_one_dimension_list(el))
        else:
            rez.append(el)
    return rez


print(to_one_dimension_list([1, [2, 3, [4,5], 6]]))
print(to_one_dimension_list([1, 2, 3]))
print(to_one_dimension_list([1, [[3]], 5]) )
