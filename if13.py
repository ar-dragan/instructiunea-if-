a=int(input("Locul ocupat de Ionel"))
if a>100:
    print("Nu primeste tricou")
elif a%4==1:
    print("alba")
elif a%4==2:
    print("rosie")
elif a%4==3:
    print("albastra")
else:
    print("neagra")