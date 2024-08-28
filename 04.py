import random

# Tietokone arpoo luvun väliltä 1..10
oikea_luku = random.randint(1, 10)

# Silmukka jatkuu, kunnes käyttäjä arvaa oikein
while True:
    # Pyydetään käyttäjää arvaamaan luku
    syote = input("Arvaa luku väliltä 1..10: ")

    # Tarkistetaan, onko syöte tyhjä
    if syote == "":
        print("Et syöttänyt yhtään lukua.")
        break

    # Yritetään muuntaa syöte kokonaisluvuksi
    try:
        arvaus = int(syote)

        # Tarkistetaan, onko arvaus välillä 1..10
        if arvaus < 1 or arvaus > 10:
            print("Syötäthän kelvollisen luvun väliltä 1..10.")
            continue

        # Tarkistetaan, onko arvaus liian suuri, liian pieni vai oikein
        if arvaus > oikea_luku:
            print("Liian suuri arvaus 1..10: 7")
        elif arvaus < oikea_luku:
            print("Liian pieni arvaus 1..10: 3")
        else:
            print("Oikein! Arvasit luvun1..10: 5")
            break
    except ValueError:
        print("Syötäthän kelvollisen luvun.")

