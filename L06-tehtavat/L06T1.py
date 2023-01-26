
# paaohjelma
def main():
    
    # kysytaan tiedoston nimi kayttajalta
    tiedostoNimi = input("Anna tallennettavan tiedoston nimi: ")
    
    # lisataan tiedostonimeen polku
    # tiedostoNimi = "./L06-tehtavat/files/" + tiedostoTemp

    # kutsutaan funktiota kirjoittamaan tiedostoon
    TiedostoKirjoita(tiedostoNimi)

    # kutsutaan funktiota lukemaan tiedoston sisalto
    TiedostoLue(tiedostoNimi)
    
    return None

        
# aliohjelma kysyy syotteen ja kirjoittaa sen tiedostoon
def TiedostoKirjoita(tiedostoNimi):
    
    # asetetaan avattu tiedosto muuttujaan
    tiedosto = open(tiedostoNimi, 'w', encoding="utf-8")

    # silmukka kysyy syotetta kayttajalta
    while(True):

        muuttuja = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
        
        # jos kayttaja syottaa nollan
        if (muuttuja == "0"):

            #suljetaan tiedosto
            tiedosto.close()
            # ja poistutaan silmukasta
            break
        
        # jos syote ei ole nolla tallennetaan se tiedostoon
        tiedosto.write(muuttuja + "\n")
    # poistutaan aliohjelmasta
    return None
   

# aliohjelma lukee luodun tiedoston sisallon
def TiedostoLue(tiedostoNimi):

    # tulostetaan pelkka tiedoston nimi, ei tiedostopolkua
    # print("Tiedostoon '" + tiedostoNimi[21:] + "' on tallennettu seuraavat nimet:")

    print("Tiedostoon '" + tiedostoNimi + "' on tallennettu seuraavat nimet:")

    # asetetaan avattu tiedosto muuttujaan
    tiedosto = open(tiedostoNimi, 'r', encoding="utf-8")

    # silmukka lukee tiedostoa kunnes tulee tyhja rivi vastaan
    while (True):

        # luetaan rivi
        rivi = tiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        
        # tulostetaan luettu rivi, ei lisata rivinvaihtoa loppuun
        print(rivi, end="")

    # suljetaan tiedosto
    tiedosto.close()

    # poistutaan aliohjelmasta
    return None

# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
