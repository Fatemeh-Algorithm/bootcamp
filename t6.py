mylist=[1,4,1,8,9,8,1]
list2=[]
max1=0
for i in mylist:
    if i not in list2:
        list2.append(i)
        #print(list2)
for j in list2:
    s=0
    for k in mylist:
        if j==k:
            s=s+1
    #print(s,j)
if s>max1:
    max1=s
print(max1)
