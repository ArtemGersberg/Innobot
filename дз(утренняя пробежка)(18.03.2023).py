a = int(input("Пробежал в первый день:"))
b = int(input("Пробег:"))
k = 1
while a<=b:
    k = k + 1
    a = a*0.1+a
print(k)