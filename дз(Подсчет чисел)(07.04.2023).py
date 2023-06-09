a=int(input("ВВедите число"))
s=0
f=0
w=0
for i in range(a):
    d=int(input())
    if d==0:
        s=s+1
    elif d>0:
        w=w+1
    else:
        f=f+1
    d==0
print("Нули:", s)
print("Положительные:",w)
print("Отрицательные:",f)

