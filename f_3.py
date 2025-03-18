def create_array(a,b,c,n):
    arr = []
    subarr = []
    strn = str(n)*c
    for i in range(b):
        subarr.append(strn)
    for i in range(a):
        arr.append(subarr)
    return arr
        
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
n = int(input("Enter a number: "))
ans = create_array(a,b,c,n)
print(f"{ans}")
