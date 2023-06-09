a,b,c = map(int,input("Введиет 3 числа").split())
if a==b==c:
    print("3")
elif a==b or a==c or b==c or b==a :
    print("2")
else:
    print("0")