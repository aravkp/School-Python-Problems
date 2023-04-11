string = input("string: ")
sum = 0
for i in string:
    if i.isdigit():
        sum += int(i)
print("sum of digits in ",string, " is ",sum)
