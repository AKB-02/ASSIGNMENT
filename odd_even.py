import random
l=[]
for i in range(10):
 l.append(random.randint(1,101))
even_list=[]
for num in l:
 if(num%2==0):
  even_list.append(num)
print(even_list)   