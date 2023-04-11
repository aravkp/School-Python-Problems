def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
def sub(x,y):
    print(x-y)
def add(x,y):
    print(x+y)

m = input("enter and operation: ")
x = int(input("enter number 1: "))
y = int(input("enter number 2: "))
if m == "*":
    mult(x,y)
elif m == "/":
    div(x,y)
elif m == "-":
    sub(x-y)
elif m == "+":
    add(x,y)





