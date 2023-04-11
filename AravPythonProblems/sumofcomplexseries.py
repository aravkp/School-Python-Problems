def power(x,n):
    return x**n
def fact(n):
    x = 1
    for j in range(1,n+1):
        x *= j
    return x
s = 1
x,n = map(int,input().split())
for i in range(1,n+1):
    sum = 1
    for b in range(1,n+1,2):
        sum += power(x,b)/fact(i)
print(sum)
