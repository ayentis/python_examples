def longest_prefix(list_words: list):
    rez = []
    for symbols in zip(*list_words):
        if len(set(symbols)) == 1:
            rez.append(symbols[0])
        else:
            break
    return ''.join(rez)



print(longest_prefix(['flower', 'flow', 'flight']))
print(longest_prefix(['car', 'cir']))
print(longest_prefix(['sol', 'ution']))