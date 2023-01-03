ekaLuku = int(input("Anna ensimmäinen luku: "))
tokaLuku = int(input("Anna toinen luku: "))

print("Laskin osaa seuraavat toiminnot:")
print("1) Summa\n2) Erotus\n3) Tulo\n4) Osamäärä\n5) Potenssi")

print("Antamasi luvut ovat", ekaLuku, "ja", tokaLuku)

valikko = input("Valitse toiminto (1-5): ")

if (valikko == "1"):
    print("Summa", ekaLuku, "+", tokaLuku, "=", (ekaLuku + tokaLuku))
elif (valikko == "2"):
    print("Erotus", ekaLuku, "-", tokaLuku, "=", (ekaLuku - tokaLuku))
elif (valikko == "3"):
    print("Tulo", ekaLuku, "*", tokaLuku, "=", (ekaLuku * tokaLuku))
elif (valikko == "4"):
    if (tokaLuku == 0):
        print("Nollalla ei voi jakaa.")
    else:
        print("Osamäärä", ekaLuku, "/", tokaLuku, "=", round((ekaLuku / tokaLuku), 2))       
elif (valikko == "5"):
    print("Potenssi", ekaLuku, "**", tokaLuku, "=", (ekaLuku ** tokaLuku))
else:
    print("Toimintoa ei tunnistettu. ")

print("Kiitos ohjelman käytöstä.")
