a = int(input("Введите номер столбца(король)"))
b = int(input("введите номер строки(король)"))
c = int(input("Введиет номер столбца"))
d = int(input("Введиет номер строки"))
if (a-c)**2==1:
    print("Yes")
elif (b-d)**2==1:
    print("Yes")
elif (c-a)**2==(d-b)**2==1:
    print("Yes")
else:
    print("No")
