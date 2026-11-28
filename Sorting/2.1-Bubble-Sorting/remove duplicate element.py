a=[5,4,8,4,2,7]
new_arr=[]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(len(a)):
    if a[i] not in  new_arr:
        new_arr.append(a[i])
print("Array without Duplicate=",new_arr)