print("Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.")
ekaLuku = int(input("Anna luku 0 ja 10 väliltä: "))
tokaLuku = int(input("Anna toinen luku 0 ja 10 väliltä: "))
kolmasLuku = int(input("Anna kolmas luku 0 ja 10 väliltä: "))

summa = ekaLuku + tokaLuku + kolmasLuku
keskiArvo = summa / 3
print("\nAntamiesi lukujen summa on ", summa, ".", sep="")
print("Antamiesi lukujen keskiarvo on ", keskiArvo, ".", sep="")
print("Keskiarvo on kokonaislukuna ", int(keskiArvo), ".", sep="")
print("Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on ", round(keskiArvo, 3), ".", sep="")
print("Kiitos ohjelman käytöstä.")
