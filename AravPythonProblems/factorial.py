import math

def factorial(n):
    for i in range(n+1):
        print(math.factorial(i),end=" ")

n = int(input("enter a number: "))
factorial(n)

