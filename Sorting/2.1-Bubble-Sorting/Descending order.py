a=[2,5,3,8,6,9]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

