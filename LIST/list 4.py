import random
numbers=[random.randint(-30,30) for i in range(30)]
positives=[num for num in numbers if num > 0]
nagative=[num for num in numbers if num < 0]
print("Original List:", numbers)
print("Positive Numbers:", positives)
print("Negative Numbers:", nagative)