arr=[10,20,0,30,40,0,50,0]
target=0
new_arr=[]
for i in arr:
    if i!=target:
        new_arr.append(i)
print(new_arr)