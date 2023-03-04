import sys


def Valikko():

    # tulostetaan valinnat    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valitse toiminto (0-3): "))
    # palautetaan kayttajan valinta
    return valikko


def LueLuku(luettavaTiedostoNimi):
    # luettavaa lukua varten lista
    luettavatLuvut = []
    try:
        # avataan luettava tiedosto muuttujaan
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        
        # silmukka tiedoston lapi kaymiseen
        while (True):
            # luetaan rivi tiedostosta ja asetetaan muuttujaan
            rivi = luettavaTiedosto.readline()
            # poista rivin lopusta rivinvaihto
            rivi = rivi[:-1]
            # jos rivilla ei ole merkkeja
            if (not(rivi.isdigit())):
                # suljetaan tiedosto
                luettavaTiedosto.close()
                # palautetaan luetut luvut
                return luettavatLuvut    
            # jos jatkuu
            else:
                # asetetaan luku listaan
                luettavatLuvut.append(int(rivi))
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + luettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # ja poistutaan ohjelmasta
        sys.exit()
    # palautetaan None
    return None    
    
    
def Summa(ekaLuku, tokaLuku):

    # lasketaan lukujen summa ja muotoillaan palautettava lause
    SummaLause = f"Summa {ekaLuku} + {tokaLuku} = {ekaLuku + tokaLuku}\n"
    # palautetaan SummaLause
    return SummaLause


def Osamaara(ekaLuku, tokaLuku):
    # jos jakaja ei ole nolla
    #if (tokaLuku != 0):
    
    # lasketaan lukujen osamaara ja muotoillaan palautettava lause
    OsamaaraLause = f"Osamäärä {ekaLuku} / {tokaLuku} = {round((ekaLuku / tokaLuku), 2)}\n"
    
    # jos jakaja on nolla
    #else:
    #    # asetetaan virhesanoma lauseeksi
    #    OsamaaraLause = "Nollalla ei voi jakaa."

    # palautetaan OsamaaraLause
    return OsamaaraLause


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista):
    try:
        # avataan kirjoitettava tiedosto muuttujaan
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        # kirjoitetaan jokainen alkio listasta
        for element in tulosLista:
            # kirjoitetaan tiedot tiedostoon
            kirjoitettavaTiedosto.write(element)
        # suljetaan kirjoitettava tiedosto
        kirjoitettavaTiedosto.close()
    except:
        # tulostetaan virheviesti
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' käsittelyssä virhe, lopetetaan.")
        # ja poistutaan ohjelmasta
        sys.exit()
    # palautetaan None
    return None
