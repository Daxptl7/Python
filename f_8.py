def convert(s):
    l = s.split(" ")
    l = list(set(l))
    l.sort()
    return l
str = input("Enter a string: ")
ans = convert(str)
print(ans)
