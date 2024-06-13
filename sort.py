a = [89,1,78,45,32,96,41]
print(f'input : {a}')
for i in range(len(a)):
    for j in range(0, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j],a[i]
    print(a)
print(f'output : {a[::-1]}')