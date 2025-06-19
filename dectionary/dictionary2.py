def check_empty_dict(mydict):
    if not mydict:
        return "The dictionary is empty"
    else:
        return "The dictionary is not empty"
mydict={}
result= check_empty_dict(mydict)
print(result)