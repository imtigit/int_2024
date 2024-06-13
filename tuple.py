a = [(3,4),(9,5),(6,2)]
b = []
for i, j in a:
    #b.append((j)*i)
    for k in range(0,i):
        b.append(j)
print(b)