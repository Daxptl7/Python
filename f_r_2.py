def binn(n):
    b = ""
    while n > 0:
        b = str(n%2) + b
        n = n // 2
    return b
n = int(input("Enter a number: "))
print(f"Binary of number {n} is: {binn(n)}")

