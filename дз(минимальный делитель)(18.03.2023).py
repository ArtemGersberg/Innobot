a = int(input("Ввелите число:"))
k=2
while (a%k) > 0:
    if a%k==0:
        print(k)
    else:
        k=k+1
print(k)

