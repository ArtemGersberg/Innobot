s=open("k7a-4.txt").readline()
k=0
m=0
for i in range(len(s)):
    if s[i] in "ABCEF":
        k=k+1
        m=max(m,k)
    else:
        k=0
print(m)