#K.Hirv
#01.11.2022
#harjutus07
import math

#programm
def kuup(a):
    print(f"Kuubi ruumala on {a**3}")

def kera(r):
    print(f"Kera ruumala on {round(4/3*math.pi*r**3,2)}")

def koonus(a,h):
    print(f"Koonuse ruumala on {round((math.pi*a**2)*h/3,2)}")

def silinder(j,h):
    print(f"Silindri ruumala on {math.pi*(j**2)*h}") 


loop = 1
while loop == 1:
    print("************** LEIAME RUUMALA **************")
    valik = int(input("1. Kuup\n2. Kera\n3. Koonus\n4. Silinder\n5. Välju\nTee valik 1-5: "))
    if valik == 1:
        a = int(input("Lisa kuubi külg: "))
        kuup(a)
    elif valik == 2:
        r = int(input("Lisa kera raadius: "))
        kera(r)
    elif valik == 3:
        a = int(input("Lisa koonuse põhja raadius: "))
        h = int(input("Lisa koonuse kõrgus: "))
        koonus(a,h)
    elif valik == 4:
        j = int(input("Lisa silndri raadius: "))
        h = int(input("Lisa slindri kõrgus: "))
        silinder(j,h)
    else:
        loop = 0


#loome argumentidega funktsiooni
def tevita(nimi="tundmatu",keel="ge"):
    if keel=="et":
        print(f"Tere {nimi}")
    elif keel=="en":
        print(f"Hi {nimi}")
    else:
        print(f"Hallo {nimi}")

tevita()
tevita("Mari","en")





