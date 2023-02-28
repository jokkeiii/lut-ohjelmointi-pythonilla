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
import L08T5Kirjasto


def main():
    # kysytaan syotteena luettavan tiedoston nimi
    luettavaTiedostoNimi = input("Anna luettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    luettavaTiedostoNimi = "./L08-tehtavat/files/" + luettavaTiedostoNimi
    # maaritetaan kirjoitettavan tiedoston nimi
    kirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    # lisataan tiedoston eteen sen polku
    kirjoitettavaTiedostoNimi = "./L08-tehtavat/files/" + kirjoitettavaTiedostoNimi
    # avataan tiedosto luettavaksi
    luettavaTiedosto = open(luettavaTiedostoNimi, 'r', encoding="utf-8")
    # avataan tiedosto kirjoitettavaksi
    kirjoitettavaTiedosto = open(kirjoitettavaTiedostoNimi, 'w', encoding="utf-8")

    # silmukka tiedoston lukua varten
    while(True):
        # luetaan rivi
        rivi = luettavaTiedosto.readline()

        # jos rivi on tyhja
        if (len(rivi) == 0):
            # poistutaan silmukasta
            break
        # poistetaan rivinvaihto
        rivi = rivi[:-1]
        # kaytetaan split funktiota hyodyksi joka tekee
        # luetusta rivista listan
        rivi = rivi.split(';')
        tulos = '{:.2f}'.format(int(rivi[1]) * float(rivi[2]),2)
        tulos = str(tulos) + "\n"
        # tulostetaan tiedot listasta
        print(tulos, end="")
        kirjoitettavaTiedosto.write(tulos)


    # suljetaan tiedostot
    luettavaTiedosto.close()
    kirjoitettavaTiedosto.close()

    # poistutaan paaohjelmasta
    return None

def Valikko():

    # tulostetaan valinnat    
    print("Mitä haluat tehdä:\n1) Lue tiedosto\n2) Analysoi tiedot\n3) Tallenna Tulokset\n0) Lopeta")
    # kysytaan kayttajalta syote
    valikko = int(input("Valintasi: "))
    # palautetaan kayttajan valinta
    return valikko

# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
