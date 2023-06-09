'''a = int(input("Возраст антона: "))
b= int(input("Возраст Бориса :"))
c = int(input("Возраст Виктора :"))
print( max(a,b,c))'''

a = int(input("Возраст антона: "))
b= int(input("Возраст Бориса :"))
c = int(input("Возраст Виктора :"))
if a>b and a>c:
    print("Антон старше Бориса и Виктора")
elif a<b and  a>c:
    print("Борис старше Антона и Виктора")
else:
    print("Виктор старше антона и Бориса")
    
