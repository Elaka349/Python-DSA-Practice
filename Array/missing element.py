arr=[1,3,4,5]
n=5
total=n*(n+1)//2
arr_sum=0
for i in range(len(arr)):
    arr_sum+=arr[i]
    missing_arr=total-arr_sum
print("missing Number=",missing_arr)