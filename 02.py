while True:

    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa ohjelman): "))

    if tuumat < 0:
        print("Negatiivinen tuumamäärä, ohjelma lopetetaan.")
        break

    sentit = tuumat * 2.54

    print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä")
