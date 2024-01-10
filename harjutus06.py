#K.Hirv
#05.12.23
#harjutus06

failike=open("s6pru_l6ustaraamatus.txt","r")

reformikad = 0
kesikud = 0
erakonnad = []

for i in failike.readlines():
    ee,pe,er,kyl = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open("nagitsad.txt","a") as fail_nagitsad:
        fail_nagitsad.write(ee + " " +pe +"\n")
        
        
print(f"Reformikaid kokku: {reformikad}")
print(f"Kesikuid kokku: {kesikud}")
print(f"Erakondi kokku: {len(erakonnad)}")


failike.close()