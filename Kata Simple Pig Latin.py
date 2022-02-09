def pig_it(string):
    rez = map(lambda word: word[1:]+word[0]+'ay' if word.isalpha() else word, string.split())
    print(" ".join(list(rez)))


pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
pig_it('Ashfdhd weywy QWewi')     # elloHay orldway !

