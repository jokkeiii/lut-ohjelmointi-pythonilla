luku = int(input("Anna kokonaisluku: "))

if (luku < 0):
    print("Luku on pienempi kuin 0.")
elif (luku < 10):
    print("Luku on pienempi kuin 10.")
else:
    print("Luku on suurempi tai yhtä suuri kuin 10.")

if ((luku % 2) == 0):
    print("Antamasi luku on parillinen.")
else:
    print("Antamasi luku on pariton.")

print("Kiitos ohjelman käytöstä.")