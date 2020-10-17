a=int(input("Dati primul numar:"))
b=int(input("Dati al doilea numar:"))
c=int(input("Dati al treilea numar:"))
if a>=0 and b>=0 and c>=0:
    if b>c:
        print(b)
    else:
        print(c)
if a<0 or b<0 or c<0:
    print(a+b)