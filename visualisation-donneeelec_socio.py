import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger ton fichier CSV
df = pd.read_csv("ensemble_elections_socio.csv")

# Assurer que 'annee' est bien de type entier
df['annee'] = df['annee'].astype(int)


# Ne garder que les colonnes numériques
df_num = df.select_dtypes(include=["float64", "int64"])

# Calcul de la matrice de corrélation
corr_matrix = df_num.corr()

# Affichage de la heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Corrélation entre les variables socio-économiques et électorales")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="chomeurs15-64ans", y="voix", hue="annee")
plt.title("Score du meilleur candidat vs Chômage (15-64 ans)")
plt.xlabel("Chômeurs 15-64 ans")
plt.ylabel("Score du candidat en tête (%)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.lmplot(data=df, x="nombres_artisant", y="voix", hue="annee", aspect=1.5)
plt.title("Score du candidat vs nombre d'artisans")
plt.xlabel("Nombre d'artisans")
plt.ylabel("Score du candidat en tête (%)")
plt.tight_layout()
plt.show()

sns.lmplot(data=df, x="nombre_de-salarie", y="voix", hue="annee", aspect=1.5)
plt.title("Score du candidat vs nombre de salariés")
plt.xlabel("Nombre de salariés")
plt.ylabel("Score du candidat en tête (%)")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="inscrits", y="inscrits_municipal", hue="annee")
plt.title("Comparaison des inscrits - Présidentielle vs Municipale")
plt.xlabel("Inscrits Présidentielle")
plt.ylabel("Inscrits Municipale")
plt.tight_layout()
plt.show()
