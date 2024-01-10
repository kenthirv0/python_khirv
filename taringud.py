# K.Hirv
# 03.01.23
# Täringud

import random

# algne raha summa
raha = 100

while True:
    while True:
        try:
            kv = int(input("Kui palju raha lauale paned? Sul on " + str(raha) + "$: "))
            if kv > 0 and kv <= raha:
                break
            else:
                print("Palun sisesta õige arv.")
            except ValueError:
                print("Palun sisesta õige arv.")

# kasutaja täringud
user_dice1 = random.randint(1, 6)
user_dice2 = random.randint(1, 6)
user_total = user_dice1 + user_dice2

# arvuti täringud
comp_dice1 = random.randint(1, 6)
comp_dice2 = random.randint(1, 6)
comp_total = comp_dice1 + comp_dice2

# leiab võitja
if user_total > comp_total:
    print("Sina võitsid, sinu numbrid olid", user_dice1, "ja", user_dice2, "mis teeb kokku", user_total)
        raha += kv
elif comp_total > user_total:
    print("Arvuti võitis, selle numbrid olid", comp_dice1, "ja", comp_dice2, "mis teeb kokku", comp_total)
        raha -= kv
else:
    print("Viik, sinu numbrid olid", user_dice1, "ja", user_dice2, "mis teeb kokku", user_total)

# kontrollib kas kasutajal on raha otsa saanud
if raha <= 0:
    print("Sul sai raha otsa. Mäng läbi.")
    break

# küsib kasutajalt kas ta soovib edasi mängida
while True:
    response = input("Kas sa soovid edasi mängida? (Y/N) ").upper()
    if response == "Y":
        break
    elif response == "N":
        print("Aitäh, et mängisid. Lõpetasid mängu " + str(money) + "$.")
        exit()
    else:
        print("Palun sisesta Y või N.")
