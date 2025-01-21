def stringinstring(str1,str2):
    if str1 in str2 :
        print("One string in the other string.")
    elif str2 in str1 :
        print("One string in the orther string.")
    else:
        print("No string are present in it") 
a=input("Enter the first string:")
b=input("Enter the secound string:")
stringinstring(a,b)        

        
    