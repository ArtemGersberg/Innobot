a = int(input("Введите номер строки(ферзь)"))
b = int(input("Введите номер столбца(ферзь)"))
c = int(input("Введите номер строки(фигура)"))
d = int(input("Введите номер столбца(фигура)"))
if (c-a)**2==(d-b)**2:
    print("Yes")
elif b==d:
    print("yes")
elif a==c:
    print("yes")
else:
    print("no")
