arr1=[10,20,30,40]
arr2=[30,40,50,60]
new_arr=[]
for i in arr1:
    if i in arr2:
        if i not in new_arr:
            new_arr.append(i)
print(new_arr)