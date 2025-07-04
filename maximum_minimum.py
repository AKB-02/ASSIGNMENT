l=[]
import random
for i in range(10):
 l.append(random.randint(1,101))
t=tuple(l)
print(f"max:{max(t)}")
print(f"min:{min(t)}")
 