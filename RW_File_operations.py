from os import strerror

content = "KYIUUIYOIUhoijhklJHoiuYOIuoiUYoihLhyoiUYioOLioIyhIUtgruyFYGUIg"

filename = input("enter filename: ")
try:
    file = open(filename, "wt")
    for s in content:
        file.write(s)
    file.close()
except IOError as e:
    print("Werror ", strerror(e))

rez = {}
try:
    file = open(filename, "rt")
    while True:
        s = file.read(1)
        if not s:
            break

        rez[s.lower()] = rez.get(s.lower(), 0) + 1

    file.close()
except IOError as e:
    print("Werror ", strerror(e))

print(rez)
rez1 = sorted(rez, key=lambda x: rez[x], reverse= True)
print(rez1)

