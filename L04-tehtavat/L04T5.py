valikko = 1
while (valikko != 0):
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Erotus\n4) Tulo\n5) Osamäärä\n6) Potenssi\n0) Lopeta")

    valikko = int(input("Valitse toiminto (0-6): "))

    if (valikko == 1):
        ekaLuku = int(input("Anna ensimmäinen luku: "))
        tokaLuku = int(input("Anna toinen luku: "))
        print("Annoit luvut", ekaLuku, "ja", tokaLuku)
    elif (valikko == 2):
        tulos = ekaLuku + tokaLuku
        print("Summa", ekaLuku, "+", tokaLuku, "=", tulos)
    elif (valikko == 3):

        tulos = ekaLuku - tokaLuku
        print("Erotus", ekaLuku, "-", tokaLuku, "=", tulos)
    elif (valikko == 4):
        tulos = ekaLuku * tokaLuku
        print("Tulo", ekaLuku, "*", tokaLuku, "=", tulos)
    elif (valikko == 5):
        if (tokaLuku == 0):
            print("Nollalla ei voi jakaa.")
            continue
        tulos = ekaLuku / tokaLuku
        print("Osamäärä", ekaLuku, "/", tokaLuku, "=", round(tulos, 2))
    elif (valikko == 6):
        tulos = ekaLuku ** tokaLuku
        print("Potenssi", ekaLuku, "**", tokaLuku, "=", tulos)
    elif (valikko == 0):
        print("Lopetetaan")
    else:
        print("Tuntematon valinta, yritä uudestaan.")
        
print("Kiitos ohjelman käytöstä.")
