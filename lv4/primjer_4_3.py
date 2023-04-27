import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

tabcorr = df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

#plt.show()

print("Najmanja cijena:")
print(df.sort_values('selling_price').tail(1))
print("Najveća cijena:")
print(df.sort_values('selling_price').head(1))

# filtriranje po godini proizvodnje
df_2012 = df[df['year'] == 2012]

# broj automobila proizvedenih 2012. godine
broj_automobila_2012 = len(df_2012)

print('Broj automobila proizvedenih u 2012. godini:', broj_automobila_2012)

# automobil s najviše kilometara
max_km = df['km_driven'].max()
car_with_max_km = df.loc[df['km_driven'] == max_km, 'name'].iloc[0]
print(f"Najviše kilometara prešao je automobil {car_with_max_km} sa {max_km} km.")

# automobil s najmanje kilometara
min_km = df['km_driven'].min()
car_with_min_km = df.loc[df['km_driven'] == min_km, 'name'].iloc[0]
print(f"Najmanje kilometara prešao je automobil {car_with_min_km} sa {min_km} km.")

common_seats = df['seats'].mode()[0]
print(f"Najčešće automobili imaju {common_seats} sjedala.")

mean_km_diesel = df.loc[df['fuel'] == 'Diesel', 'km_driven'].mean()
mean_km_petrol = df.loc[df['fuel'] == 'Petrol', 'km_driven'].mean()

print(f"Prosječna kilometraža za automobile s dizel motorom iznosi {mean_km_diesel:.2f} km.")
print(f"Prosječna kilometraža za automobile s benzinskim motorom iznosi {mean_km_petrol:.2f} km.")

print(df.columns)




