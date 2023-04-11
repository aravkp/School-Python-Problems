n = int(input("enter a number : "))
sum = 0
for i in range(1,n+1):
    print("1/",i**3,"\n+")
    sum = sum + (1/(i**3))
print(" = \n", sum)
    
