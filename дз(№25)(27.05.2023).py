a=open("k7a-5.txt").readline()
m=0
k=0
for i in range(len(a)):
    if a[i] in "ABDE":
        k=k+1
        m=max(m,k)
    else:
        k=0
print(m)