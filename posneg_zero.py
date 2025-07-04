p=n=z=0
for i in range(10):
 num=int(input(f"enter integer"))
 if num>0:
  p=p+1
 elif num<0:
  n=n+1
 else:
  z=z+1
print(f"positive num:{p}")
print(f"negative num:{n}")
print(f"zeros num:{z}")