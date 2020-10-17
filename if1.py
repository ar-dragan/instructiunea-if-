n1=int(input("dati numarul primului elev:"))
p1=int(input("dati puncatjul primului elev:"))
n2=int(input("dati numarul al doilea elev:"))
p2=int(input("dati puncatjul al doilea elev:"))
n3=int(input("dati numarul al treilea elev:"))
p3=int(input("dati puncatjul al treilea elev:"))
if p1>p2 and p1>p3:
    print(n1)
if p2>p1 and p2>p3:
    print(n2)
if p3>p1 and p3>p2: 
    print(n3)
if p1==p2 and p1>p3 and p2>p3:
    print(n1,n2)
if p2==p3 and p2>p1 and p3>p1:
    print(n2,n3)
if p1==p3 and p1>p2 and p3>p2:
    print(n1,n3)
if p1==p2==p3:
   print(n1,n2,n3)