import os

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __str__(self):
        return "Bad line"


class FileEmpty(StudentsDataException):
    def __str__(self):
        return "File empty"


#filename = input("filename : ")
filename = "2.txt"
rez = {}
try:

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        raise FileEmpty

    file = open(filename, "rt")
    for s in file.readline():
        arr = s.split()
        if len(arr) != 3:
            raise BadLine
        st_name = f"{arr[0]} {arr[1]}"
        try:
            rez[st_name] = rez.get(st_name, 0) + float(arr[2])
        except TypeError:
            raise BadLine

    print(rez)

except IOError as e:
    print("File err: ", os.strerror(e.errno))
except BadLine as e:
    print("Line err: ", e)
except FileEmpty as e:
    print("Empty err: ", e)
except Exception as e:
    print("Un err: ", e)

