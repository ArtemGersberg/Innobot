a = int(input("Введите число пирожков:"))
b = int(input("Введите стоимость пирожка (кол-во рублей):"))
c = int(input("Введите стоимость пирожка (кол-во копеек):"))
if a*c>=100:
    print("Кол-во рублей:", a*b+((a*c)//100),"кол-во копеек:", (a*c)%100)
else:
    print("Кол-во рублей:", a*b,"кол-во копеек:", a*c)
