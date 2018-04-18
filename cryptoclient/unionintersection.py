a = [1,2,3,4]
b = [4,5,6]
c = a
d = []
k = False
for i in b:
    k = False
    for j in c:
        if i == j:
            d.append(i)
            k = True
            break

    if k == False:
        c.append(i)

print('Union is  ', c)
print('Intersection is ', d)