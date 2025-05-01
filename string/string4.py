def remove_first_occurrence(a, b):
    return a.replace(b, '')

a = input("Enter a string: ")
b = input("Enter a substring to remove: ")
f = remove_first_occurrence(a,b)
print(f) 
