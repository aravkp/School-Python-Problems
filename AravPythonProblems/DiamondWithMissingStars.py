n = 3
k = 0
for i in range (1, n + 1):
    space = (n - i)*" "
    print(space, end=' ')
    while (k != (2 * i - 1)) :
        if (k == 0 or k == 2 * i - 2) : 
            print('*', end= "") 
        else : 
            print(' ', end = "") 
        k = k + 1
    k = 0
    print()
for j in range (n - 1, 0, -1):
    space = (n - j)*" "
    print(space, end=" ")
    k = (2 * j - 1)
    while (k > 0) :
        if (k==1 or k == 2*j-1):
            print("*",end="")
        else:
            print(" ",end="")
        k = k - 1
    print()
