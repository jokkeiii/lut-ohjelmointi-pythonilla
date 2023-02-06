######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 01/02/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def main():
    # kysytaan tiedoston nimi
    tiedostoNimi = input("Anna tiedoston nimi: ")
    # lisataan tiedostopolku
    #tiedostoNimi = "./L07-tehtavat/files/" + tiedostoNimi
    # avataan tiedosto luettavaksi
    tiedosto = open(tiedostoNimi, 'r', encoding="utf-8")
    # luetaan ensimmainen rivi pois alta
    rivi = tiedosto.readline()

    # silmukka tiedoston lukua varten
    while(True):
        # luetaan rivi
        rivi = tiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # poistetaan rivinvaihto
        rivi = rivi[:-1]
        # kaytetaan split funktiota hyodyksi joka tekee
        # luetusta rivista listan
        rivi = rivi.split(';')
        # tulostetaan tiedot listasta
        print("Kello oli " + rivi[2] + ", kun punnittiin marjoja " + rivi[0] + ".")


    # suljetaan tiedosto
    tiedosto.close()

    # poistutaan paaohjelmasta
    return None
    
# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
