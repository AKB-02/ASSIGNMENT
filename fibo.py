n=int(input("enter the num of terms:"))
a,b=0,1
if n<=0:
 print(f("please enter positive integers"))
elif n==1:
 print(a)
elif n==2:
 print(a)
 print(b)
else:
 print(a)
 print(b)
 for i in range(2,n):
  c=a+b
  print(c)
  a,b=b,c  