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

    # esitellaan lista
    ostoslista = []
    
    # valikon valinta muuttuja
    valinta = '1'

    # silmukka kunnes valinta on 0
    while (valinta != '0'):

        # kutsutaan aliohjelmaa
        valinta = valikko(ostoslista)
        
        # jos valinta on 1
        if (valinta == '1'):
            # kysytaan syote ja lisataan se listaan
            tuote = input("Anna lisättävä tuote: ")
            ostoslista.append(tuote)
            print()
        # jos valinta on 2
        elif (valinta == '2'):
            # tulostetaan tuotteiden maara
            print("Ostoslistassasi on", len(ostoslista), "tuotetta.")
            # kysytaan syote
            poistoNumero = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            # poistetaan listasta kyseinen tuote 
            del ostoslista[poistoNumero - 1]
            print()
        # jos valinta on 0
        elif (valinta == '0'):
            # tulostetaan listan sisalto
            print("Sinulta jäi ostamatta seuraavat tuotteet:\n", ostoslista, sep="")

    # poistutaan paaohjelmasta
    return None


def valikko(ostoslista):

    # tulostetaan listan sisalto
    print("Ostoslistasi sisältää seuraavat tuotteet:\n", ostoslista, sep="")
    
    # tulostetaan valikkovaihtoehdot
    print("Voit valita alla olevista toiminnoista:\n1) Lisää\n2) Poista\n0) Lopeta")
      
    # kysytaan syote
    valinta = input("Valintasi: ")
    
    # jos syote on 1, 2 tai 0
    if (valinta == '1' or valinta == '2' or valinta == '0'):
        # palautetaan valinta
        return valinta
    else:
        # tulostetaan virheviesti
        print("Tunnistamaton valinta.\n")
        # palautetaan valinta
        return valinta
    
    


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")