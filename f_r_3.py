'''
def vowell(s):
    count = 0
    a = "aeiouAEIOU"
    for i in s:
        if i in a:
            count+=1
    return count
s = input("Enter a string: ")
ans= vowell(s)
print(f"The number of vowel in string {s} is {ans}")
'''
def vowell(s):
    a = "aeiouAEIOU"
    if s[0] in a:
        return 1 + vowell(s[1:])
    else:
        return vowell(s[1:])
s = input("Enter a string: ")
print(f"Number of vowel in string {s} is {vowell(s)}")

