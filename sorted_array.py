def sort_array(arr):
    odd = [(arr[i],i) for i in range(len(arr)) if (arr[i] % 2)]
    odd_list, odd_pos = zip(*odd)
    odd = zip(sorted(odd_list),odd_pos)
    for x in odd:
        arr[x[1]] = x[0]
    return(arr)



sort_array([3, 1]) #-> [1, 3]
sort_array([3, 2, -1, 4])# -> [-1, 2, 3, 4]
sort_array([5, 3, 2, 8, 1, 4])# -> [1, 3, 2, 8, 5, 4]
sort_array([0, -1, -2, -3, 4, 1])# -> [0, -3, -2, -1, 4, 1]