a=[5,4,3,2,1]
passes=0
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    passes+=1
print(a)
print("pass=",passes)