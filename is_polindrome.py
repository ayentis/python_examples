text = input("text ").replace(" ","").upper()
rez = bool(text)
for i in range(len(text) // 2):
    if text[i] != text[-i-1]:
        rez = False
        break
print(rez)