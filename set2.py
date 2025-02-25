import random
s=set()
while(len(s)<20):
    s.add(random.randint(15,46))
print(s)
count=0
l=list(s)
for i in l:
    if(i<30):
        count +=1
l=[i for i in l if i<35]
s=set(l)
print("Total number for elemets:",count)
print("Set after all opration:",s)