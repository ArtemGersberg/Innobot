a=int(input("Введите число:"))
k=0
while a>0:
    k=k+a%10
    a=a//10
print(k)