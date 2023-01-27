# aloita kommentointi

def main():
    
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna tiedot sisältävän tiedoston nimi: ")

    # lisataan tiedoston eteen sen polku
    luettavaTiedostoNimi = "./L06-tehtavat/files/" + luettavaTiedostoNimi

    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna tallennettavan tiedoston nimi: ")

    # lisataan tiedoston eteen sen polku
    kirjoitettavaTiedostoNimi = "./L06-tehtavat/files/" + kirjoitettavaTiedostoNimi
    
    # kutsutaan aliohjelmaa laskemaan riveista askelien kokonaismaara
    askelMaara = LaskeAskelMaara(luettavaTiedostoNimi)

    # kutsutaan aliohjelmaa laskemaan suurin askelien maara
    suurinAskelMaara = LaskeSuurinAskelMaara(luettavaTiedostoNimi)

    # kutsutaan aliohjelmaa laskemaan pienin askelien maara
    pieninAskelMaara = LaskePieninAskelMaara(luettavaTiedostoNimi)

    # tulostetaan lasketut askelien maarat
    print("Pienin askelmäärä oli", pieninAskelMaara, "askelta.")

    print("Suurin askelmäärä oli", suurinAskelMaara, "askelta.")

    print("Yhteensä askelia oli", askelMaara, "askelta.")

    # kutsutaan aliohjelmaa kirjoittamaan maarat tiedostoon
    KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, pieninAskelMaara, suurinAskelMaara, askelMaara)

    # poistutaan ohjelmasta
    return None


def LaskeAskelMaara(luettavaTiedostoNimi):

    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")

    # askelmaaran laskemiseen muuttuja
    askelMaara = 0

    # silmukka kunnes tiedosto loppuu
    while (True):

        # luetaan rivi tiedostosta ja asetetaan muuttujaan
        rivi = luettavaTiedosto.readline()

        # jos rivilla ei ole merkkeja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # jos jatkuu
        else:
            # poista rivin lopusta rivinvaihto
            rivi = rivi[:-1]
            askelMaara += int(rivi)

    # suljetaan luettava tiedosto
    luettavaTiedosto.close()

    # palautetaan askelien maara
    return askelMaara
    

def LaskeSuurinAskelMaara(luettavaTiedostoNimi):

    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")

    # suurimman askelmaaran laskemiseen muuttuja
    suurinAskelMaara = 0

    # luetaan ensimmainen rivi
    rivi = int(luettavaTiedosto.readline()[:-1])

    # ja asetetaan se suurinAskelMaara muuttujaan
    suurinAskelMaara = rivi

    # silmukka kunnes tiedosto loppuu
    while (True):

        # luetaan rivi tiedostosta ja asetetaan muuttujaan
        rivi = luettavaTiedosto.readline()

        # jos rivilla ei ole merkkeja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        
        # poista rivin lopusta rivinvaihto
        rivi = int(rivi[:-1])

        # jos rivi on suurempi kuin suurinAskelMaara
        if (rivi > suurinAskelMaara):

            # aseta rivi suurinAskelMaara muuttujaan
            suurinAskelMaara = rivi
        
    # suljetaan luettava tiedosto
    luettavaTiedosto.close()

    # poistutaan ohjelmasta
    return suurinAskelMaara


def LaskePieninAskelMaara(luettavaTiedostoNimi):

    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    
    # pienimman askelmaaran laskemiseen muuttuja
    pieninAskelMaara = 0

    # luetaan ensimmainen rivi
    rivi = int(luettavaTiedosto.readline()[:-1])

    # ja asetetaan se suurinAskelMaara muuttujaan
    pieninAskelMaara = rivi

    # silmukka kunnes tiedosto loppuu
    while (True):

        # luetaan rivi tiedostosta ja asetetaan muuttujaan
        rivi = luettavaTiedosto.readline()

        # jos rivilla ei ole merkkeja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # jos jatkuu
    
        # poista rivin lopusta rivinvaihto
        rivi = int(rivi[:-1])
        
        # jos rivi on suurempi kuin suurinAskelMaara
        if (rivi < pieninAskelMaara):

            # aseta rivi suurinAskelMaara muuttujaan
            pieninAskelMaara = rivi

    # suljetaan luettava tiedosto
    luettavaTiedosto.close()

    # poistutaan ohjelmasta
    return pieninAskelMaara


def KirjoitaTiedostoon(kirjoitettavaTiedostoNimi, pieninAskelMaara, suurinAskelMaara, askelMaara):
    
    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")
    
    # asetetaan kirjoitettava teksti muuttujaan
    kirjoitettavaTeksti = "Pienin askelmäärä oli " + str(pieninAskelMaara) + " askelta.\n"
    
    # kirjoitetaan tiedot tiedostoon
    kirjoitettavaTiedosto.write(kirjoitettavaTeksti)

    # asetetaan kirjoitettava teksti muuttujaan
    kirjoitettavaTeksti = "Suurin askelmäärä oli " + str(suurinAskelMaara) + " askelta.\n"

    kirjoitettavaTiedosto.write(kirjoitettavaTeksti)

    # asetetaan kirjoitettava teksti muuttujaan
    kirjoitettavaTeksti = "Yhteensä askelia oli " + str(askelMaara) + " askelta.\n"

    kirjoitettavaTiedosto.write(kirjoitettavaTeksti)

    # suljetaan tiedosto
    kirjoitettavaTiedosto.close()

    # poistutaan ohjelmasta
    return None


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")