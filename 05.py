oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

maksimi_yritykset = 5

yritykset = 0

while yritykset < maksimi_yritykset:

    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

    if yritykset == maksimi_yritykset:
        print("Pääsy evätty.")
