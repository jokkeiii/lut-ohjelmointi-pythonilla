# aloita kommentointi

def main():

    # valikon muuttuja
    valinta = 1

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = Valikko()

        # jos valinta on 1
        if (valinta == 1):

            # kysytaan kayttajalta luvut
            sanoma = "Anna ensimmäinen luku: "
            ekaLuku = AnnaLuku(sanoma)
            sanoma = "Anna toinen luku: "
            tokaLuku = AnnaLuku(sanoma)

            # tulostetaan annetut luvut
            print("Annoit luvut", ekaLuku, "ja", tokaLuku)

        # jos valinta on 2
        elif (valinta == 2):

            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            summaLause = Summa(ekaLuku, tokaLuku)
            # tulostetaan aliohjelman palautus
            print(summaLause)

        # jos valinta on 3
        elif (valinta == 3):

            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            osamaaraLause = Osamaara(ekaLuku, tokaLuku)
            # tulostetaan aliohjelman palautus
            print(osamaaraLause)
        # jos valinta on 0
        elif (valinta == 0):
            # tulostetaan lopetusviesti
            print("Lopetetaan")
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")


def Valikko():

    # tulostetaan valinnat    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valitse toiminto (0-3): "))
    # palautetaan kayttajan valinta
    return valikko


def AnnaLuku(sanoma):

    # palautetaan kayttajalta kysytty syote,
    # sanoma tulostus argumenttina
    return int(input(sanoma))


def Summa(ekaLuku, tokaLuku):

    # lasketaan lukujen summa ja muotoillaan palautettava lause
    summaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}"
    # palautetaan summalause
    return summaLause

def Osamaara(ekaLuku, tokaLuku):

    # jos jakaja ei ole nolla
    if (tokaLuku != 0):
        # lasketaan lukujen osamaara ja muotoillaan palautettava lause
        osamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}"
    # jos jakaja on nolla
    else:
        # asetetaan virhesanoma lauseeksi
        osamaaraLause = "Nollalla ei voi jakaa."
    
    # palautetaan osamaaralause
    return osamaaraLause


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
