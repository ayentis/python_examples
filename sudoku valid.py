v1 = [
    295743861,
    431865927,
    876192543,
    387459216,
    612387495,
    549216738,
    763524189,
    928671354,
    154938672,
]

v2 = [
    195743862,
    431865927,
    876192543,
    387459216,
    612387495,
    549216738,
    763524189,
    928671354,
    254938671,
]

rez = '123456789'


def check_str1(matrix: list) -> bool:
    rez = filter(lambda s: "".join(sorted(str(s))) == rez, matrix)
    return list(rez)


def check_str(matrix: list) -> bool:

    for s in matrix:
        if "".join(sorted(str(s))) != rez:
            return False
    return True


def check_row1(matrix: list) -> bool:

    rez = []


    for col in range(9):
        s = [str(row)[col] for row in matrix]
        if "".join(sorted(s)) != rez:
            return False
    return True


def check_row(matrix: list) -> bool:
    for col in range(9):
        s = [str(row)[col] for row in matrix]
        if "".join(sorted(s)) != rez:
            return False
    return True


def check_squere(matrix: list) -> bool:

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            s = str(matrix[row])[col:col+3] \
                + str(matrix[(row+1)])[col:col+3]\
                + str(matrix[(row+2)])[col:col+3]



            if "".join(sorted(s)) != rez:
                return False
    return True


def check_matrix(matrix: list) -> bool:
    return check_str(matrix) and check_row(matrix) and check_squere(matrix)


print(check_row1(v1))

# print(check_matrix(v1))
# print(check_matrix(v2))
