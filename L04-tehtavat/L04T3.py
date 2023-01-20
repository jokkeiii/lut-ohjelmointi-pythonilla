aMuuttuja = int(input("Anna a:n arvo: "))

bMuuttuja = int(input("Anna b:n arvo: "))

print("a:", aMuuttuja, "b:", bMuuttuja)

jatka = True

while (jatka == True):
    aMuuttuja *= 2
    bMuuttuja += 100
    print("a:", aMuuttuja, "b:", bMuuttuja)
    if (aMuuttuja > bMuuttuja or aMuuttuja > 10000 or bMuuttuja > 10000):
        jatka = False

print("Kiitos ohjelman käytöstä.")
