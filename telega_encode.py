
def encode(st: str) -> str:
    st_up = st.upper()
    rez = []
    for s in st_up:
        if s == " ":
            rez.append(s)
        elif st_up.count(s) == 1:
            rez.append("(")
        else:
            rez.append(")")
    x = "".join(rez)
    #
    print(x)
    return x

encode('no rep*at')# -> '(( (((((('
encode('HeLlo world!')# -> '(())) ()()(('
encode(' ')# -> ' '