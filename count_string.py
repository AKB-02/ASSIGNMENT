name=input("enter a string")
uniq=set(name)
d={}
for s in uniq:
 d[s]=name.count(s)
print(d)
 