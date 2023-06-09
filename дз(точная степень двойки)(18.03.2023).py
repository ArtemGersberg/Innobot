a = int(input("Введите число"))
k = 0
f = 0
s= a/2
while a != 1:
    a = a/2
    k = k+1
    if a%2==0:
        if a==2:
            print("Yes")
            break
        else:
            continue
    else:
        print("No")
        break
if a==(1 or 2):
    print("Yes")


