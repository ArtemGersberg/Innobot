a = float(input("Вклад:"))
b = float(input("Процент:"))
c = float(input("Не менее:"))
k=0
while a<c:
    a=(a*(b/100)+a)//1
    k=k+1
print(k)
