def frequency(s):
    fdict = {}
    for word in s.split():
        word = word.lower()
        if word in fdict:
            fdict[word] += 1
        else:
            fdict[word] = 1
    return dict(sorted(fdict.items()))

s = input("Enter a string: ")
print(frequency(s))
