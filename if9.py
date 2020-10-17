xa=int(input("Introduceti numarul bilelor albe mari:"))
xr=int(input("Introduceti numarul bilelor rosii mari:"))
xv=int(input("Introduceti numarul bilelor verzi mari:"))
ya=int(input("Introduceti numarul bilelor albe mici:"))
yr=int(input("Introduceti numarul bilelor rosii mici:"))
yv=int(input("Introduceti numarul bilelor verzi mici:"))

xt=xa+xr+xv
print("numarul total de bile mari=",xt)
yt=ya+yr+yv
print("numarul total de bile mici=",yt)
print("in total sunt",xt+yt,"bile")
if xt>yt:
    print("Mai multe sunt bile mari")
elif yt>xt:
    print("Mai multe sunt bile mici")
else:
    print("Bilele sunt egale")
if (xa+ya)>(xr+yr) and (xa+ya)>(xv+yv):
    print("mai multe sunt bile albe")
elif(xr+yr)>(xa+ya) and (xr+yr)>(xv+yv):
    print("mai multe sunt bile rosii")
elif(xv+yv)>(xa+ya) and (xv+yv)==(xr+yr):
    print("mai multe sunt bile verzi")
elif(xa+ya)==(xr+yr) and (xa+ya)>(xv+yv):
    print("mai multe sunt bile albe si rosii")
elif(xv+yv)==(xr+yr) and (xv+yv)>(xa+ya):
    print("mai multe sunt bile verzi si rosii")
elif(xv+yv)==(xa+ya) and (xv+yv)>(xr+yr):
    print("mai multe sunt bile verzi si albe")
else:
    print("toate bilele dupa culori sunt egale")