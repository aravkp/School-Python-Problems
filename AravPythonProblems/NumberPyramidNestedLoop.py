n=5
for i in range(1,n+1):
    spaces = (n-i)*" "
    print(spaces,end="")
    for k in range(i,1,-1):
        print(k,end="")
    for j in range(1,1+i):
        print(j,end="")
    print()
