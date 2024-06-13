#invertpyramid
def pyra_pattern(inn):
    for i in range(1, inn+1):
        for j in range(inn-i): #spaces code
            print(' ',end = '')
        for k in range(1, 2*i):
            print('*', end='')
        print()
    #pyramid
    for i in range(inn, 0, -1):
        for j in range(inn-i): #spaces code
            print(' ',end = '')
        for k in range(2*i-1):
            print('*', end='')
        print()
inn = int(input('Enter number of pattern : '))
pyra_pattern(inn)
