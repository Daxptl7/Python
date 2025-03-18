def ispangram(s):
    alpha = {chr(x) for x in range(65,91)}
    if set(s.upper()).issuperset(alpha):
        return True
    else:
        return False
s = "The quick brown fox jumps over the lazy dog"
ans = ispangram(s)
print(f"{ans}")
