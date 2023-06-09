a=int(input("ВВедите число"))
s=0
for i in range(len(str(a))):
    s=s+a%10*2**i
    a=a//10
print(s)