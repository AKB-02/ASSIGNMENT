a=int(input("enter a num"))
b=True
if a<=1:
 b=False
else:
 for i in range(2,int(a**0.5+1)):
  if a%i==0:
   b=False
   break
if b==True:
 print("prime")
else:
 print("not prime")