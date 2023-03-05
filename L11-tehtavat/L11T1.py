######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joakim Ijäs
# Opiskelijanumero: 001063376
# Päivämäärä: 05/03/2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def main():
    luku = int(input("Anna luku: "))
    if luku <= 0:
        print("Luku ei voi olla nolla tai negatiivinen.")
    else:
        alku = 0
        while True:
            tulos = alku ** 2
            if tulos == luku:
                print("Neliöjuuri on", alku)
                break
            elif tulos > luku:
                if  (luku - ((alku - 1) ** 2)) < (luku - tulos):
                    print("Neliöjuuri on", alku - 1)
                    break
                else:
                    print("Neliöjuuri on", alku)
                    break 
            alku += 1
    # poistutaan paaohjelmasta
    return None
    # or (luku - ((alku - 1) ** 2)) < (luku - tulos)
# kutsutaan paaohjelmaa
main()

# tulostetaan lopputervehdys
print("Kiitos ohjelman käytöstä.")
