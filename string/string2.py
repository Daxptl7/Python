def to_lowercase(s):
    result1=""
    for i in s:
        if 'A'<=i<='Z':
            result1+=chr(ord(i)+32)
        else:
            result1+=i
    return result1
def to_uppercase(s):
    result=""
    for i in s:
        if 'a'<=i<='z':
            result+=chr(ord(i)-32)
        else:
            result+=i
    return result

text1=input("Enter the string for convert to lowercase:")
text2=input("Enter the string for convert to uppercase:")
print("Lowercase string is:",to_lowercase(text1))
print("Uppercase string is:",to_uppercase(text2),end=" ")