import pandas as pd
import numpy as np

mtcars = pd.read_csv('mtcars.csv')

sort_mpg = mtcars.sort_values(by=['mpg'])
najveci_mpg = sort_mpg.tail(5)
print(najveci_mpg)

sort_mpg2 = mtcars.sort_values(by=['mpg', 'cyl'])
najmanja_mpg = sort_mpg2.head(3)
print(najmanja_mpg.query('cyl == 8'))

srednja_potrosnja = (mtcars.query('cyl == 6')).mean()
print("Srednja potrosnja automobila s 6 cilindara: ", srednja_potrosnja['mpg'])

srednja_potrosnja2 = (mtcars.query('cyl == 4'))
srednja_potrosnja3 = (srednja_potrosnja2.query('wt <= 2.200'))
srednja_potrosnja4 = (srednja_potrosnja3.query('wt >= 2.000')).mean()
print("Srednja potrosnja automobila s 4 cilindara: ", srednja_potrosnja4['mpg'])

mjenjac = (mtcars.query('am == 0')).count()
print("Manualni mjenjac: ", mjenjac['am'])
mjenjac2 = (mtcars.query('am == 1')).count()
print("Automatski mjenjac: ", mjenjac2['am'])

zad = (mtcars[(mtcars.am == 1) & (mtcars.hp > 100)]).count()
print("Broj automobila s auto i preko 100: ", zad['car'])


mtcars["mass_kg"] = mtcars["wt"] * 1000 * 0.45392
print(mtcars[["car", "mass_kg"]])



