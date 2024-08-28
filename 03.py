luvut = []

while True:
    syote = input("Anna luku (tyhjä merkkijono lopettaa): ")

    if syote == "":
        break

    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötäthän kelvollisen luvun.")

if luvut:

    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")
