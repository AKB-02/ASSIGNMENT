print("calc menu:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

a=input("choose operation ")
b=float(input("enter num:"))
c=float(input("enter num:"))

if a=='1':
 print(f"result:{b+c}")
elif a=='2':
 print(f"result:{b-c}")
elif a=='3':
 print(f"result:{b*c}")
elif a=='4':
 if c!=0:
  print(f"result:{b/c}")
 else:
  print("error cannot divide")
else:
 print("Invalid choice")