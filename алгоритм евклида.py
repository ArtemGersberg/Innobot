a, b = map(int, input("Введиет 2 чила").split())
k =0
s=0
while a!=0 and b!=0:
    if a>b:
        a= a%b
        k = k+1
    else:
        b = b%a
        k=k+1
if a==0:
    print("Нод=", b)
else:
    print("Нод=", a)
while a != b:
    if a>b:
        a=a-b
        s = s+1
    else:
        b = b-a
        s = s+1
print("Обычный:",k )
print("Модифицированный:",s)

