a,b = map(int,input("Введите стоимость товара ").split())
c,d = map(int,input("Внесено ").split())
if b<d:
    print(c-a,d-b)
elif b>d:
    print(c-a-1,100+d-b)
else:
    print(c-a,d-b)
