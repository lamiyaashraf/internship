t=(1,2,3,4,5)
l=list(t)
for i in range(len(l)):
    l[i]*=2
result=tuple(l)
print(t)
print(result)