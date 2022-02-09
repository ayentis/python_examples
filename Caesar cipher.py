str = input("enter str ")
while True:
    try:
        shift = int(input("enter shift (1..25) "))
        break
    except:
        print("incorrect input, try again")

rez = []
for sym in str:
    ord_sym = ord(sym)
    if (ord_sym >= ord("A")
            and ord_sym <= ord("Z")):
        ord_sym += shift
        if ord_sym > ord("Z"):
            ord_sym += ord("A") - ord("Z") - 1
        rez.append(chr(ord_sym))
    elif (ord_sym >= ord("a")
            and ord_sym <= ord("z")):
        ord_sym += shift
        if ord_sym > ord("z"):
            ord_sym += ord("a") - ord("z") -1
        rez.append(chr(ord_sym))
    else:
        rez.append(sym)

print("".join(rez))

# cdezabCDEzab 123