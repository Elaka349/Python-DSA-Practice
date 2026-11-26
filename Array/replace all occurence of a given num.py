arr=[10,20,30,20,40,20,50]
target=20
new_arr=77
for i in range(len(arr)):
    if arr[i]==target:
        arr[i]=new_arr
print(arr)