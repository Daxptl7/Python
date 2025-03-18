def create_list(list1, list2):
    intersection = [i for i in list1 if i in list2]
    return intersection
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = create_list(list1, list2)
print(result)
