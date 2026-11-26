arr=[10,20,30,20,40,50,20]
new_arr=[]
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)