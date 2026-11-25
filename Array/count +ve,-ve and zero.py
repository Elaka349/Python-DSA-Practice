arr=[-8,20,-2,0,-10,45]
pos=0
neg=0
zero=0
for i in arr:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print("Positive=",pos)
print("Negative=",neg)
print("Zero=",zero)            
        