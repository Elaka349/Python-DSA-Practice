a=[1,2,3,4,5]
sorted_array=True
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            sorted_array=False
            break
if sorted_array:
    print("Array is already sorted")
else:
    print("Array is not sorted")
