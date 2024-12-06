a="Hello world from Python"
print(a[: : -1])
new={}
for i in a:
    if i.isalpha():
        new[i]=new.get(i,0)+1
print(new)
result=""
for i in a:
    if i not in result:
        result +=i
print(result)
