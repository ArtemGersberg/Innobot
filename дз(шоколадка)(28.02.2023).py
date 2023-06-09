a = int(input())
b = int(input())
c = int(input())
if c%b==0 or c%a==0:
    print("yes")
elif a*b<c:
    print("no")
else:
    print("no")
