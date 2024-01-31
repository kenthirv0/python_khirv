# Python KT
# Kent Hirv
#31.01.24

# 1. Korrutamise kontrollimine
# 	programm esitab korrutustehte 1p
# 	ootab kasutajalt vastuse sisestamist 1p
# 	kontrollib vastuse õigsust 1p
# 	väljastab, kas vastus oli õige või väär. 1p
# 	kokku antakse lahendamiseks 10 ülesannet.


import random

def korrutamise_kontroll():
    oiged_vastused = 0
    kokku = 10

    for _ in range(kokku):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        tehe = num1 * num2

        vastus = int(input(f"Mis on {num1} korda {num2}? "))

        if vastus == tehe:
            print("Õige!")
            oiged_vastused += 1
        else:
            print(f"Vale, õige vastus on {tehe}.")

    print(f"Vastasid {oiged_vastused} tehet {kokku} st õigesti.")

korrutamise_kontroll()

# 3. Positiivsed ja negatiivsed
# 	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 
# 	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab
# 	nulli lisamisel ei tehta midagi
# 	väljasta mõlemad loendit

# Loendite loomine
positiivsed = []
negatiivsed = []

# Kasutaja sisestab 5 arvu
for _ in range(5):
    arv = int(input("Sisesta arv: "))

    # Tuvastab, kumba loendisse arvu lisada
    if arv > 0:
        positiivsed.append(arv)
    elif arv < 0:
        negatiivsed.append(arv)

# Väljastab mõlemad loendid
print("Positiivsed arvud:", positiivsed)
print("Negatiivsed arvud:", negatiivsed)


# 5. Ostunimekiri
# Looge programm, mis jälgib ostunimekirja esemeid. Programm peaks küsima uusi
# elemente seni, kuni midagi ei sisestata (ei sisestata, millele järgneb sisestus-/tagasiklahv).
# Seejärel peaks programm kuvama täieliku ostunimekirja.

nimekiri = []

# Küsi kuni midagi pole lisatud
while True:
    item = input("Sisesta asi mida lisada nimekirja (või jäta tühjaks): ")
    if item == "":
        break
    nimekiri.append(item)

# Display the full shopping list
print("Shopping List:")
for item in nimekiri:
    print(item)


# 7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti
# 	küsitakse valuuta kogust ja tehakse arvutused
# 	kood kommenteeritud

def eurokalkulaator():
    print("Vali valuuta tüüp:")
    print("1. EUR -> EEK")
    print("2. EEK -> EUR")

    valik = int(input("Sisesta valik (1 või 2): "))

    if valik == 1:
        eurod = float(input("Sisesta eurode summa: "))
        eek = eurod * 15.6466
        print(f"{eurod} eurot on {eek} krooni.")
    elif valik == 2:
        kroonid = float(input("Sisesta kroonide summa: "))
        eurod = kroonid / 15.6466
        print(f"{kroonid} krooni on {eurod} eurot.")
    else:
        print("Vigane valik! Palun sisesta 1 või 2.")

eurokalkulaator()


# 9. Emaili kontroll
# 	kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll
# 	programm tükeldab selle ja väljastab lause: "Tere enimi, sinu email on server serveris ja domeeniks on sul com"
# 	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad

email = input("Sisesta email: ")

if "@" in email:
    parts = email.split("@")
    username = parts[0]
    server = parts[1].split(".")[0]
    domain = parts[1].split(".")[1]
    print(f"Tere {username}, sinu email on server {server} ja domeeniks on sul {domain}.")
else:
    print("Vigane emaili formaat!")


# 11. Salakeel
# 	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida
# 	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks
# 	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks

def create_secret_language():
    word = input("Sisesta tavaline sõna: ")
    secret_word = ""

    for letter in word:
        if letter.lower() in "aeiou":
            secret_word += letter + "p" + letter.lower()
        else:
            secret_word += letter

    print(f"Salakeel: {secret_word}")


def translate_secret_language():
    secret_word = input("Sisesta salakeeles sõna: ")
    word = ""

    i = 0
    while i < len(secret_word):
        if secret_word[i].lower() in "aeiou":
            word += secret_word[i]
            i += 2
        else:
            word += secret_word[i]
            i += 1

    print(f"Tõlge: {word}")


def secret_language():
    choice = input("Kas soovid salakeelt luua või tõlkida? (luua/tõlkida): ")

    if choice.lower() == "luua":
        create_secret_language()
    elif choice.lower() == "tõlkida":
        translate_secret_language()
    else:
        print("Vigane valik! Palun sisesta 'luua' või 'tõlkida'.")


secret_language()


# 13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja  vastus
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli
# 	kood mis teavitab paaris või paaritust arvust
# 	kuvatakse programmi pealkiri

def check_even_odd():
    print("Kasutaja sisestab arvu ja programm kontrollib, kas arv on paaris või paaritu.")
    number = input("Sisesta arv: ")

    if number.isdigit():
        number = int(number)
        if number == 0:
            print("Sisestatud arv on null.")
        elif number % 2 == 0:
            print("Sisestatud arv on paaris.")
        else:
            print("Sisestatud arv on paaritu.")
    else:
        print("Vigane sisend! Palun sisesta arv.")

print("Arvu paarsuse kontrollija")
check_even_odd()


# 15. Temperatuurid - Programm peab töötlema ühe aasta kõigi päevade temperatuure.
# Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupäeval oli kõige soojem.
# Väljasta kuupäev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu päeva, väljasta vähemalt üks)

temperatures = {
    "jaanuar": [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3],
    "veebruar": [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18],
    "märts": [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2],
    "aprill": [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2],
    "mai": [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1],
    "juuni": [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22],
    "juuli": [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20],
    "august": [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11],
    "september": [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19],
    "oktoober": [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1],
    "november": [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1],
    "detsember": [-15, 2, -11, -14, -15, -5, -5, -18, -18, -19, 0, 0, 2, -7, -16, -7, -4, -1, -1, -16, -18, -10, -3, -19, -6, -16, -16, -8, -2, -18]
}

months = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

for month in months:
    temperatures_month = temperatures[month]
    max_temperature = max(temperatures_month)
    max_temperature_index = temperatures_month.index(max_temperature)
    date = max_temperature_index + 1
    print(f"{month.capitalize()}: Kõige soojem päev oli {date}. kuupäeval, temperatuuriga {max_temperature} kraadi.")


# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud õigesti
# 	Programm tükeldab selle ja väljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com

def check_email():
    email = input("Sisesta email: ")

    if "@" in email and "." in email:
        username, domain = email.split("@")
        server, extension = domain.split(".")
        print(f"Tere {username}, sinu email on server {server}is ja domeeniks on sul {extension}.")
    else:
        print("Vigane email! Palun sisesta email õiges formaadis.")

check_email()
