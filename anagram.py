t1 = sorted(input("t1 ").replace(" ","").upper())
t2 = sorted(input("t2 ").replace(" ","").upper())

if t1 == t2 and t1:
    print("anagram")
else:
    print("not anagram")