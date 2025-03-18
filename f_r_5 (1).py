def powerr(a,b):
    if b == 0:
        return 1
    return a * powerr(a,b-1)

ma = int(input("Enter a number: "))
hi = int(input("Enter another number: "))
print(powerr(ma,hi))
