a=int(input("primul numar"))
b=int(input("al doilea numar"))
c=int(input("al treilea numar"))
if ((a%2==0)and(b%2==0)and(c%2==0)):
    print(a,"Par")
    print(b,"Par")
    print(c,"Impar")
elif ((a%2==0)and(b%2==0)and(c%2!=0)):
    print(a,"Par")
    print(b,"Par")
    print(c,"Impar")
elif ((a%2==0)and(b%2!=0)and(c%2==0)):
    print(a,"Par")
    print(b,"Impar")
    print(c,"Par")
elif ((a%2!=0)and(b%2==0)and(c%2==0)):
    print(a,"Impar")
    print(b,"Par")
    print(c,"Par")
elif ((a%2!=0)and(b%2!=0)and(c%2==0)):
    print(a,"Impar")
    print(b,"Impar")
    print(c,"Par")
elif ((a%2!=0)and(b%2==0)and(c%2!=0)):
    print(a,"Impar")
    print(b,"Par")
    print(c,"Imapr")
elif ((a%2==0)and(b%2!=0)and(c%2!=0)):
    print(a,"Par")
    print(b,"Impar")
    print(c,"Impar")
else:
    print(a,"Impar")
    print(b,"Impar")
    print(c,"Impar")