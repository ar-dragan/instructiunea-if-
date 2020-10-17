a=int(input("Dati primul numar:"))
b=int(input("Dati al doilea numar:"))
if (a%2)==0 and (b%2)==0:
    if a>b:
        print(a)
    else :
        print(b)
if (a%2)==0 and (b%2)!=0:
    print(a)
if (a%2)!=0 and (b%2)==0:
        print(b)
if (a%2)!=0 and (b%2)!=0:
    print("NU AVEM NUMERE PARE")
