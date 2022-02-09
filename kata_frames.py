def frame(text, char):
    maxlen = max([len(x) for x in text])

    rez = char*(maxlen+4)+'\n'
    for current_text in text:
        rez += char+' '+current_text+' '*(maxlen-len(current_text))+' '+char+"\n"
    rez += char * (maxlen + 4)

    return rez

print(frame(['Smaller', 'frame'], '~'))
print(frame(['Create','this','kata'], '+'))