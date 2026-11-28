a=[1,2,3,4,6,5]
for i in range(len(a)-1):
  swapped=False
  for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            swapped=True
  if swapped==False:
    break
print("Sorted array",a)
