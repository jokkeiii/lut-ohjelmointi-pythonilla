######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 03/03/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


def main():
    # listat lukemista ja tallentamista varten
    luettuLista = []
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # luettavaTiedostoNimi = "./L09-tehtavat/files/" + luettavaTiedostoNimi
    # virheenkasittely
    try:
        # avataan tiedosto luettavaksi
        luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
        # silmukka tiedoston lukua varten
        while(True):
            # luetaan rivi
            rivi = luettavaTiedosto.readline()
            # jos rivi on tyhja
            if (len(rivi) == 0):
                # poistutaan silmukasta
                break
            # lisataan rivi listaan
            luettuLista.append(rivi)
        # suljetaan tiedosto
        luettavaTiedosto.close()
        # aliohjelman lopetusviesti
        print("Tiedoston '", luettavaTiedostoNimi, "' lukeminen onnistui, ", len(luettuLista), " riviä.", sep="")
    except:
        print("Tiedoston '", luettavaTiedostoNimi, "' käsittelyssä virhe, lopetetaan.", sep="")
        return None
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    # kirjoitettavaTiedostoNimi = "./L09-tehtavat/files/" + kirjoitettavaTiedostoNimi
    try:
        # avataan tiedosto kirjoitettavaksi
        kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
        for element in luettuLista:
            # kirjoitetaan tiedot tiedostoon
            kirjoitettavaTiedosto.write(element)
        # suljetaan tiedosto
        kirjoitettavaTiedosto.close()
        # tulostetaan aliohjelman lopetusviesti
        print("Tiedoston '" + kirjoitettavaTiedostoNimi + "' kirjoittaminen onnistui.", sep="")
    except:
        print("Tiedoston '", kirjoitettavaTiedostoNimi, "' käsittelyssä virhe, lopetetaan.", sep="")
        return None
    # tulostetaan lopputervehdys
    print("Kiitos ohjelman käytöstä.")
    # poistutaan paaohjelmasta
    return None


# kutsutaan paaohjelmaa
main()
