a=[7,9,3,5,2,1]
for i in range(len(a)-1):
    for j in range(len(a)-0-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)