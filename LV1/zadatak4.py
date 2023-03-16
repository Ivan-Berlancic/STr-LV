
brojac = 0
lista = []
ime_datoteke = input("Unesite ime datoteke: ")
fhand = open(ime_datoteke)
print("Ime datoteke: mbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        words = line.split()
        lista.append(words[1])
        brojac = brojac + float(words[1])
print("Average X-DSPAM-Confidence: ", brojac/len(lista))
fhand.close()
    