# aloita kommentointi

def main():
    
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")

    # lisataan tiedoston eteen sen polku
    luettavaTiedostoNimi = "./L06-tehtavat/files/" + luettavaTiedostoNimi

    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = "L06T3T1.txt"

    # lisataan tiedoston eteen sen polku
    kirjoitettavaTiedostoNimi = "./L06-tehtavat/files/" + kirjoitettavaTiedostoNimi
    
    # avataan luettava tiedosto muuttujaan
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")

    # avataan kirjoitettava tiedosto muuttujaan
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")

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
        
        # jos rivilla on numeroita
        if (rivi.isdigit()):
            # tulostetaan rivin sisalto
            print("Rivi '", rivi, "' on numerorivi.", sep="")

        # jos rivin sana on palindromi
        elif (rivi == rivi[::-1]):
            # tulostetaan rivin sisalto
            print("Rivi '", rivi, "' on palindromi.", sep="")
            # kirjoitetaan rivi tiedostoon
            kirjoitettavaTiedosto.write(rivi + "\n")

        # jos rivin sana ei ole palindromi
        else:
            # tulostetaan rivin sisalto
            print("Rivi '", rivi, "' ei ole palindromi.", sep="")

    # poistutaan paaohjelmasta
    return None

    # suljetaan luettava tiedosto
    luettavaTiedosto.close()

    # suljetaan kirjoitettava tiedosto
    kirjoitettavaTiedosto.close()

# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")