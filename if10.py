ng=int(input("Numarul de gaini"))
nb=int(input("Numarul total de boabe"))
nbg=nb//ng
nbc=nb-(ng*nbg)
if nbg>nbc:
    print("Gaina primeste mai mult cu",nbg-nbc,"boabe")
elif nbc>nbg:
    print("Curcanul primeste mai mult cu",nbc-nbg,"boabe")
else:
    print("primesc acelasi numar de boabe")