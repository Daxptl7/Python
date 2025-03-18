def count_lower_upper(s):
    upper =0
    lower = 0
    for ch in s:
        if ch > chr(96):
            lower+=1
        elif ch>chr(64):
            upper+=1
        else:
            print("More then one word")
    print(f"Lower case in string {s} is {lower}, uppercase are {upper}")
s = input("Enter a string: ")
count_lower_upper(s)
