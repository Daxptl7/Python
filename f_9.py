def count_alpha_digits(s):
    alpha = 0
    count = 0
    for char in s:
        if char.isalpha():
            alpha += 1
        elif char.isdigit(): 
            count += 1
    return alpha, count

s = input("Enter a string: ")
alpha, digit = count_alpha_digits(s)
print(f"Alphabets are: {alpha}, Digits are: {digit}")
