# aloita kommentointi

def main():

    # esitellaan lista
    ostosLista = []
    
    # valikon valinta muuttuja
    valinta = '1'

    while (valinta != '0'):
        valinta = valikko()
        
        if (valinta == '1'):
            tuote = input("Anna lisättävä tuote: ")
            ostosLista.append(tuote)
    
    # poistutaan paaohjelmasta
    return None


def valikko():

    # tulostetaan listan sisalto
    print("Ostoslistasi sisältää seuraavat tuotteet:\n", ostosLista)
    
    # tulostetaan valikkovaihtoehdot
    print("Voit valita alla olevista toiminnoista:\n1) Lisää\n2) Poista\n0) Lopeta")

    # valikko silmukka
    while (True):    
        
        # kysytaan syote
        valinta = input("Valintasi: ")
        
        # jos syote on 1, 2 tai 0
        if (valinta == '1' or valinta == '2' or valinta == '0'):
            # poistutaan silmukasta
            break
        # 
        else:
            # tulostetaan virheviesti
            print("Tunnistamaton valinta.")
    
    # palautetaan valinta
    return valinta


# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
