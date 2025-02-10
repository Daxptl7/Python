import random 
numbers=[random.randint(0,30) for i in range(50)]
print("Original List:", numbers)
uniqed_list=list(set(numbers))
print("Unique List:", uniqed_list)