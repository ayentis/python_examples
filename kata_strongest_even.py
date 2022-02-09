def strongest_even(n, m):
    while m & m - 1 >= n:
        print(m, m - 1, m & m - 1)
        m &= m - 1
    return m

print(strongest_even(19, 29))

