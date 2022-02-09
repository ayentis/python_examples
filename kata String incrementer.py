def increment_string1(strng):
    num = "".join([s for s in strng if s.isdigit()])
    word = "".join([s for s in strng if s.isalpha()])
    numstr = "1"
    if num:
        numstr = str(int(num) + 1)
    maxlen = max(len(num), len(numstr))
    print (f"{word}{numstr.rjust(maxlen,'0')}")


def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    print( head + str(int(tail) + 1).zfill(len(tail)))

# increment_string("foo")#, "foo1")
# increment_string("foobar0a01")#, "foobar002")
# increment_string("foobar1")#, "foobar2")
# increment_string("foobar00")#, "foobar01")
# increment_string("foobar99")#, "foobar100")
# increment_string("foobar099")#, "foobar100")
# increment_string("")#, "1")
increment_string("tdFrCiyHURSCYGw85071714729022537931717890361648859474849805220732")
increment_string1("tdFrCiyHURSCYGw85071714729022537931717890361648859474849805220732")
