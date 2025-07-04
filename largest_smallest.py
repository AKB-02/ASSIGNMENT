a=input("enter num in seperated by spaces")
b=[int(num)for num in a.split()]
largest=b[0]
smallest=b[0]
for num in b:
 if num>largest:
  largest=num
 if num<smallest:
  smallest=num
print(f"largest:{largest}")
print(f"smallest:{smallest}")