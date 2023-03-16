radni_sati = int(input("Unesite broj radnih sati: "))
satnica = int(input("Unesite koliko ste plaćeni po radnom satu: "))
#rezultat = int(radni_sati) * int(satnica)


def total_euro(radni_sati, satnica):
    rez = radni_sati * satnica
    return rez


print("Zaradili ste: ", total_euro(radni_sati, satnica))
