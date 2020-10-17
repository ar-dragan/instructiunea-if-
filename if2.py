a=int(input("introduceti prima latura:"))
b=int(input("introduceti a doua latura:"))
c=int(input("introduceti a treia latura:"))
if a<b+c and b<a+c and c<a+b:
    print("da")
else:
    print("nu")