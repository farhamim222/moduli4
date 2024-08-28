import random
def laske_pi(pisteiden_maara):
    ympyraan_osuneet = 0

    for _ in range(pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            ympyraan_osuneet += 1

    pi_likiarvo = 4 * ympyraan_osuneet / pisteiden_maara
    return pi_likiarvo

pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))

pi_likiarvo = laske_pi(pisteiden_maara)
print(f"Piin likiarvo (käyttäen {pisteiden_maara} pistettä) on: {pi_likiarvo:.6f}")
