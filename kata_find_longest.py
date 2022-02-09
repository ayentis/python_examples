def find_longest(string):
    lw = max(string.split(), key=len)
    return lw


print(find_longest("The quick white fox jumped around the 645645564646 massive dog"))