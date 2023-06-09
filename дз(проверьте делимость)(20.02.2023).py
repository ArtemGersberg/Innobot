a,b = map(int,input("Введите число").split())
print((a-(a//b*b)+b-(b//a*a)-(b%a+a%b))+1)
