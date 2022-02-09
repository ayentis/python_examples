def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")
            else:
                print("I don't with you")

f = psychologist()

next(f)
f.send('hello')
f.send('bad')
f.send('good')
f.send('good?')
f.send('hello')
f.send('bad')
f.send('good')
f.send('good?')
