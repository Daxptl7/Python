a=input("Enter the string")
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
vowels_count=a.lower()
for i in vowels_count:
    if i in vowels:
        vowels[i]+=1

print(f"Vowels count in the string is:{vowels}")