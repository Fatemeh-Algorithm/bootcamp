mylist=[1,4,1,8,9,1]
max1=0
for i in mylist:
    if i>max1:
        max1=i
        mylist.remove(i)
        print(max1)
      
