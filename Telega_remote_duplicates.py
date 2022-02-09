def remove_duplicates(lst):
    return [x for x in lst if lst.count(x) == 1]



remove_duplicates([1, 2, 1, 2])# -> []
remove_duplicates([1, 2, 1, 3])# -> [2, 3]
remove_duplicates([2, 5, 6, 7, 5, 2, 6])# -> [7]