num = int(input("enter a number: "))
maxi = num
mini = num
for i in range(1,5):
    num = int(input("enter a number: "))
    if num > maxi:
        maxi = num
    elif num < mini:
        mini = num
print("maximum = ",maxi,"\nminimum = ",mini)
    
