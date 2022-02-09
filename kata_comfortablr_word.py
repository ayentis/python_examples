groups = (
    'wsxol',
    'edcik',
    'rtf',
    'gvb',
    'yuh',
    'jnm',
    'qazp'
)


def comfortable_word(word):

    return len(set([elem for letter in word for elem in groups if letter in elem])) == len(word)



# print(comfortable_word('yams'))
# print(comfortable_word('test'))
print(comfortable_word('their'))

