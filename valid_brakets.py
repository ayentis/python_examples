def solution(s: str) -> list:

    arr=[]
    for ch in s:
        if (len(arr) > 0 and arr[-1] == '(' and ch == ')'):
            arr.pop()
        else:
            arr.append(ch)

    return arr


print(solution('()')) #True
print(solution(')()')) # False
print(solution('(')) # False
print(solution('(())((()())())')) # True