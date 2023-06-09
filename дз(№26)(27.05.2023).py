a=open("k7a-6.txt").readline()
m=0
k=0
for i in range(len(a)):
    if a[i] in "BCDF":
        k=k+1
        m=max(k,m)
    else:
        k=0
print(m)