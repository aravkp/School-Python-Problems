def titler(string):
    list1 = list(string)
    words = 0
    for i in list1:
        if i == " ":
            words +=1
    if words >= 1:
        print(string.title())
