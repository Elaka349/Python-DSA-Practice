arr=[10,20,30,40,20,50]
target=20
new_arr=[]
for i in arr:
    if i!=target:
        new_arr.append(i)
print(new_arr)