ac=int(input("dati anul curent:"))
lc=int(input("dati luna curent:"))
zc=int(input("dati ziua curent:"))
an=int(input("dati anul nasterii:"))
ln=int(input("dati luna nasterii:"))
zn=int(input("dati ziua nasterii:"))
if ln>lc:
   print(ac-an+1,"ani")
else:
   print(ac-an,"ani")