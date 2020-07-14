lst=[2]
for j in range(3, 101):
    control=True
    for i in range(2, j):
        if j%i == 0:
            control=False
            break
    if control==True:
        lst.append(j)
print(lst)