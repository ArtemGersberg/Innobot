a = int(input("Введите номер строки(слон)"))
b = int(input("Введите номер столбца(слон)"))
c = int(input("Введите номер строки(фигура)"))
d = int(input("Введите номер столбца(фигура)"))
if (a-c==2 or a-c==-2) and (b-d==-1 or b-d==2) :
    print("Yes")
elif (b-d==2 or b-d==-2) and (a-c==1 or a-c==-1) :
    print("Yes")
else:
    print("no")
