a,b = map(int,input("Введите координаты 1ой точки").split())
c,d = map(int,input("Введите координаты 2ой точки").split())
if (a and c) > 0 and (b and d)>0:
    print("Yes")
elif (a and c)<0 and (b and d)<0:
    print("Yes")
elif (a and c)<0 and (b and d)>0:
    print("Yes")
elif (a and c)>0 and (b and d)<0:
    print("Yes")
else:
    print("No")
