
indeksi = 0
arvosana = 0
summa = 0
while (arvosana != -1):
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    if (arvosana != -1 and (arvosana < 1 or arvosana > 5)):
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
        continue
    elif (arvosana == -1):
        break
    summa += arvosana
    indeksi += 1

# keskiarvo ei jostain syysta toimi
keskiarvo = summa / indeksi

print("Arvosanojen keskiarvo on ", round(keskiarvo, 2), ".", sep="")

print("Kiitos ohjelman käytöstä.")
