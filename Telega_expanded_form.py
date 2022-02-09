
def expanded_form(digit):
    st = str(digit)[::-1]
    x = enumerate(st)
    lst = ' + '.join([str(int(s)*10**i) for i, s in enumerate(str(digit)[::-1]) if int(s) != 0][::-1])
    # lst = ' + '.join([s.zfill(i+1)[::-1] for i, s in enumerate(str(digit)[::-1]) if int(s) != 0][::-1])
    # lst = [st[i].zfill(i+1)[::-1] for i in range(len(st)) if int(st[i]) != 0]
    print(lst)

expanded_form(1)# -> '1'
expanded_form(1234)# -> '1000 + 200 + 30 + 4'
expanded_form(1001)# -> '1000 + 1'