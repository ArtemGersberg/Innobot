a,b,c = map(int,input("Введиет кол-во часов, минут и секунд:").split())
d,e,f = map(int,input("Введиет кол-во часов, минут и секунд:").split())
print("Разница во времени( в секундах):",(d*3600+e*60+f)-(a*3600+b*60+c))
