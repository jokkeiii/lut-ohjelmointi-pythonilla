######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 28/02/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
import L09T4Kirjasto


def main():

    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # luettavaTiedostoNimi = "./L09-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L09-tehtavat/files/" + kirjoitettavaTiedostoNimi

    # luettavien lista
    lukuLista = []
    # kirjoitettavien lista
    tulosLista = []
    # valikon muuttuja
    valinta = 1
    # laskuri lukulistassa etenemistä varten
    lukuLaskuri = 0

    # valikko silmukka
    while (valinta != 0):

        # kutsutaan valikko aliohjelmaa ja asetetaan palautus muuttujaan
        valinta = L09T4Kirjasto.Valikko()

        # jos valinta on 1
        if (valinta == 1):
            # jos lukuja ei ole viela luettu tiedostosta
            if (lukuLaskuri == 0):
                # luetaan luvut
                lukuLista = L09T4Kirjasto.LueLuku(luettavaTiedostoNimi)
                # tulostetaan lukuviesti
                # print("Luettu tiedosto '" + luettavaTiedostoNimi[:-11] + "'.")
                # codegrade versio
                print("Luettu tiedosto '" + luettavaTiedostoNimi + "'.")
                # asetetaan luvut laskettaviksi muuttujiin
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                # tulostetaan luvut
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                # lisataan laskuriin seuraavia lukuja varten
                lukuLaskuri += 2
            # jos kaikki listan luvut on jo luettu
            elif (lukuLaskuri + 1 > len(lukuLista)):
                print("Luvut loppuivat, lopeta ohjelma.")
            # kun luvut ovat listassa
            else:
                # asetetaan luvut laskettaviksi muuttujiin
                ekaLuku = lukuLista[lukuLaskuri]
                tokaLuku = lukuLista[lukuLaskuri + 1]
                # tulostetaan luvut
                print("Luettiin luvut", ekaLuku, "ja", tokaLuku)
                # lisataan laskuriin seuraavia lukuja varten
                lukuLaskuri += 2
        # jos valinta on 2
        elif (valinta == 2):
            # kutsutaan summa aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = L09T4Kirjasto.Summa(ekaLuku, tokaLuku)
            # lisataan kirjoitettavaTeksti listaan
            tulosLista.append(kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos lisätty listaan.")
        # jos valinta on 3
        elif (valinta == 3):
            # kutsutaan osamaara aliohjelmaa ja asetetaan palautus muuttujaan
            kirjoitettavaTeksti = L09T4Kirjasto.Osamaara(ekaLuku, tokaLuku)
            # lisataan kirjoitettavaTeksti listaan
            tulosLista.append(kirjoitettavaTeksti)
            # tulostetaan viesti
            print("Tulos lisätty listaan.")

        # jos valinta on 0
        elif (valinta == 0):
            if (len(tulosLista) == 0):
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
            else:
                # kutsutaan aliohjelmaa kirjoittamaan listan sisalto tiedostoon
                L09T4Kirjasto.KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, tulosLista)
                # tulostetaan lopetusviesti
                # print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi[:-11] + "'.")
                # codegrade versio
                print("Tallennettu tiedosto '" + kirjoitettavaTiedostoNimi + "'.")
        # jos valinta ei ole 1, 2, 3 tai 0
        else:
            print("Tuntematon valinta, yritä uudestaan.")

    # palautetaan None
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
