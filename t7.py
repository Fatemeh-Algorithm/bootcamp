mylist=['eat','tea','tan','ate','nat','bat']
result=[]
for i in mylist:
    g = []
    for j in mylist:
        if sorted(i) == sorted(j):
            if j not in group:
                g.append(j)
    if g not in result:
        result.append(g)

print(result)
