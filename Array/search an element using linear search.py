arr=[10,20,30,40,50]
target=30
found=False
for i in range (len(arr)):
    if arr[i]==target:
        found=True
        break
if found:
    print("element is found")
else:
    print("Element not found")        