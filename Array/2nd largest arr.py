arr=[89,10,45,99,12,27]
largest=float('-inf')
smallest=float('-inf')
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("second_largest=",second)


        
        