try:
    ocjena = float(input("Unesite ocjenu od 0.0 do 1.0: "))

    if ocjena >= 0.9 and ocjena <= 1.0 and ocjena >= 0.0:
        print("Kategorija: A")
    elif ocjena >= 0.8 and ocjena <= 1.0 and ocjena >= 0.0:
        print("Kategorija: B")
    elif ocjena >= 0.7 and ocjena <= 1.0 and ocjena >= 0.0:
        print("Kategorija: C")
    elif ocjena >= 0.6 and ocjena <= 1.0 and ocjena >= 0.0:
        print("Kategorija: D")
    elif ocjena < 0.6 and ocjena <= 1.0 and ocjena >= 0.0:
        print("Kategorija: F")
    else:
        print("Krivi unos")
except Exception:
    print("Niste unijeli broj")