s1 = input("s1 ")
s2 = input("s2 ")

def pos(s1: str, s2: str) -> bool:
    pos = 0
    for ch in s1:
        pos = s2.find(ch,pos)
        if pos == -1:
            return False
    return True

print(pos(s1,s2))