lista = []
broj = 0
brojac = 0
while broj != "Done":
    broj = input("Unesite broj: ")
    if broj.isdigit():
        lista.append(broj)
        brojac = brojac + int(broj)
print(lista)

print("Broj elemenata liste: ", len(lista))
br = len(lista)
print("Srednja vrijednost: ", brojac/br)

lista.sort()
print(lista)

print("Minimum:", min(lista))
print("Maksimum:", max(lista))