def q1():
    list1 = list(map(str,input().split(" ")))
    n = input("enter an element")
    print(list1.count(n))

def q2():
    list1 = list(map(int, input().split(" ")))
    pos = []
    neg=[]
    for i in list1:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    print("all are ",list1)
    print("positives are ",pos)
    print("negatives are " ,neg)

def q3():
    list1 = list(map(int,input().split()))
    print(max(list1))

def q4():
    list1 = list(map(int,input().split()))
    list1.remove(max(list1))
    print(max(list1))

def q5():
    list1 = list(map(int,input().split()))
    list1.sort()
    mid = len(list1) // 2
    res = (list1[mid] + list1[~mid]) / 2
    print(str(res))

def q6():
    list1 = list(map(int,input().split()))
    list1.sort()
    newlist = []
    for i in list1:
        if list1.count(i)>1:
            list1.remove(i)
    print(list1)

def q7():
    list1 = list(map(int,input().split(" ")))
    p,x = (map(int,input().split(" ")))
    list1.insert(p,x)
    print(list1)

def q8a():
    list1 = list(map(int,input().split(" ")))
    x = int(input())
    list1.pop(x)
    print(list1)

def q8b():
    list1 = list(map(int,input().split(" ")))
    x = int(input())
    list1.remove(x)
    print(list1)

def q9():
    list1 = list(map(int,input().split(" ")))
    list1.reverse()
    print(list1)
