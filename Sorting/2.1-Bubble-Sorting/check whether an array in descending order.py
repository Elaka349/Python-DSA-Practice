arr=[5,4,3,2,1]
flag=True
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        flag=False
        break
if flag:
    print("Descending order")
else:
    print("Not descending order")

       