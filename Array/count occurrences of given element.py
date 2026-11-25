arr=[10,20,30,20,50,20]
target=20
count=0
for i in range(len(arr)):
    if arr[i]==target:
        count+=1
print("Total count=",count)
