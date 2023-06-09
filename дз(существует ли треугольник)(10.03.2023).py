a,b,c = map(int,input("Введите стороны треугольника").split())
if a==b+c or b==a+c or c==a+b:
    print("No")
else:
    print("Yes")