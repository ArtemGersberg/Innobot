n=input("Введите буквы")
k=0
for i in range(len(n)):
    if n[i]=="a":
        n = n[:i] + "b" + n[i + 1:]
        k = k + 1
    elif n[i]=="A":
        n = n[:i] + "B" + n[i + 1:]
        k = k + 1
print(n)
print(k)