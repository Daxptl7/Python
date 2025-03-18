def tup(x):
    lst = [(x,x**2,x**3) for x in range(1,x+1)]
    print(lst)
x = int(input("Enter a number: "))
tup(x)
