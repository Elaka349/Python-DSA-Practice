a=[1,7,5,3,9]
count=0
for i in range(len(a)-1):
    for j in range (len(a)-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count+=1
print("Descending order=",a)            
print("count=",count)