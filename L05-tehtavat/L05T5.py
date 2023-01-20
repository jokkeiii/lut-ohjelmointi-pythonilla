def main():

    valinta = 1

    while (valinta != 0):

        valinta = Valikko()

        if (valinta == 1):

            sanoma = "Anna ensimmäinen luku: "
            ekaLuku = AnnaLuku(sanoma)
            sanoma = "Anna toinen luku: "
            tokaLuku = AnnaLuku(sanoma)

            print("Annoit luvut", ekaLuku, "ja", tokaLuku)

        elif (valinta == 2):

            summaLause = Summa(ekaLuku, tokaLuku)
            print(summaLause)

        elif (valinta == 3):

            osamaaraLause = Osamaara(ekaLuku, tokaLuku)
            print(osamaaraLause)
        elif (valinta == 0):
            print("Lopetetaan")
        else:
            print("Tuntematon valinta, yritä uudestaan.")



def Valikko():
    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    valikko = int(input("Valitse toiminto (0-3): "))
    return valikko

def AnnaLuku(sanoma):

    return int(input(sanoma))

def Summa(ekaLuku, tokaLuku):

    summaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}"
    return summaLause

def Osamaara(ekaLuku, tokaLuku):

    if (tokaLuku != 0):
        osamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}"
    
    else:
        osamaaraLause = "Nollalla ei voi jakaa."
    return osamaaraLause

main()

print("Kiitos ohjelman käytöstä.")
