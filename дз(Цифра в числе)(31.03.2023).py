a=int(input("ВВедите число:"))
b=int(input("ВВедите число:"))
k=0
while a>0:
    if a%10==b:
        k=k+1
    a=a//10
print(k)