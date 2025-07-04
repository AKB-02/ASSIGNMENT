names=["a","a","b","b","b","c","d"]
d={}
for name in names:
 if name not in d.keys():
  d[name]=names.count(name)
print(d)  