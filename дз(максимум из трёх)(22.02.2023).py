a,b,c = map(int,input("введите 3 числа через пробел").split())
if a==b==c:
    print("они равны")
else:
    print(max(a,b,c))
