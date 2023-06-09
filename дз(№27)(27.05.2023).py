a=open("k7b-1.txt").readline()
a=a.replace("C"," ").replace("D"," ")
k=0
m=0
for i in range(len(a)):
    if a[i]=="E":
        if a[i+1]=="A":
            if a[i+2]=="B":
                k=k+1
                m=max(k,m)
    else:
        k=0
print(m)
