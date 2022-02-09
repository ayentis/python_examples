dat = input("input data YYYYMMDD ")

if dat.isdigit():
    while True:
        rez = sum([int(x) for x in dat])
        if rez < 10:
            break
        dat = str(rez)

    print("Digit of life ", rez)
else:
    print("wrong format")
