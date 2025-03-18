def pfactor(n,d=2):
    if n <= 1:
        return []
    if n % d == 0:
        return [d] + pfactor(n // d, d)
    else:
        return pfactor(n, d+1)
n = int(input("Enter a positive integer: "))
result = pfactor(n)
print(f"Prime factors of {n} are --> {result}")
