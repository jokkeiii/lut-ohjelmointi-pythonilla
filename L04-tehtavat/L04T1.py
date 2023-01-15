aloitusArvo = int(input("Anna aloitusarvo: "))

lopetusArvo = int(input("Anna lopetusarvo: "))

print("Toteutus for-lauseella:")

for i in range(aloitusArvo, lopetusArvo + 1):
    print(i, end=" ")

i = aloitusArvo

print("\n\nToteutus while-lauseella:")

while (i != lopetusArvo + 1):
    print(i, end=" ")
    i += 1

print("\n\nKiitos ohjelman käytöstä.")
