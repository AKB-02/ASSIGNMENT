n=int(input("enter a num"))
og=n
s=0
while n>0:
 r=n%10
 s=s*10+r
 n=n//10
if s==og:
 print("palindrome")
else:
 print("not palindrome") 