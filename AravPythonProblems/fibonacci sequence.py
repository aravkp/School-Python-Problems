s=[0,1]
num=int(input("num of terms"))
n=0
for i in range(num-2):
    s.append(s[n]+s[n+1])
    n=n+1
print(s)
