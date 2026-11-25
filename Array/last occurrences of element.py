arr=[10,20,30,20,20,50]
target=20
last=-1
for i in range(len(arr)):
    if arr[i]==target:
        last=-i
print("last occurrences index:",last)
    