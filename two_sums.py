
def two_sum(l,rez):
    # for i in range(len(l)):
    #     for j in range(i+1,len(l)):
    #         if (l[i]+l[j] == rez):
    #             return [i,j]
    return [[i,j] for i in range(len(l)) for j in range(i+1,len(l)) if l[i]+l[j] == rez][0]


print(two_sum([2, 7, 11, 15], 9)) #-> [0, 1]
print(two_sum([3, 2, 4], 6)) #-> [1, 2]
print(two_sum([0, 4, 3, 0], 0)) #-> [0, 3]