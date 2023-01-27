# aloita kommentointi
import math

def main():
    
    tiedostoNimi = input("Anna luettavan tiedoston nimi: ")

    # lisataan tiedostonimeen polku
    #tiedostoNimi = "./L06-tehtavat/files/" + tiedostoNimi

    # kutsutaan funktiota laskemaan rivien maara
    riviMaara = laskeRivit(tiedostoNimi)
    
    # kutsutaan funktiota laskemaan merkkien maara
    merkkiMaara = laskeMerkit(tiedostoNimi)

    print("Tiedostossa oli", riviMaara, "nimeä ja", merkkiMaara, "merkkiä.")

    # lasketaan nimista pituuskeskiarvo ja pyoristetaan kokonaisluvuksi
    nimiKeskiarvo = round((merkkiMaara - riviMaara) / riviMaara)

    print("Keskimääräinen nimen pituus oli", nimiKeskiarvo, "merkkiä.")
    return None


def laskeRivit(tiedostoNimi):

    # asetetaan avattu tiedosto muuttujaan
    tiedosto = open(tiedostoNimi, 'r', encoding="utf-8")

    riviMaara = 0

    # silmukka lukee tiedostoa kunnes tulee tyhja rivi vastaan
    while (True):

        # luetaan rivi
        rivi = tiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):

            # poistutaan silmukasta
            break
        else:
            riviMaara += 1

    # suljetaan tiedosto
    tiedosto.close()

    # poistutaan aliohjelmasta
    return riviMaara


def laskeMerkit(tiedostoNimi):

    # asetetaan avattu tiedosto muuttujaan
    tiedosto = open(tiedostoNimi, 'r', encoding="utf-8")

    merkkiMaara = 0

    # silmukka lukee tiedostoa kunnes tulee tyhja rivi vastaan
    while (True):

        # luetaan rivi
        rivi = tiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        else:

            # rivinvaihtomerkki pois
            #rivi = rivi[:-1]
            # lisataan merkkien maara muuttujaan
            merkkiMaara += len(rivi)

    # suljetaan tiedosto
    tiedosto.close()

    # poistutaan aliohjelmasta
    return merkkiMaara

# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
