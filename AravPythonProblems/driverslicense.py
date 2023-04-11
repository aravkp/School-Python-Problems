name = input("what is your name: ")
age = int(input("enter age: "))
if age >=18:
    print(name,", you are eligible!")
else:
    print(name,", try in ", 18-age," years")
