import pandas as pd

# Charger les fichiers socio-économiques et les données finales
df_socio_eco = pd.read_csv("donnees_socio_fusionnees.csv", sep=";")  # fichier socio-économique
df_final = pd.read_csv("ensemble_elections.csv")  # fichier des élections


# Créer la colonne 'CODGEO' dans df_final en combinant 'code_dept' et 'code_com'
df_final["CODGEO"] = df_final["code_dept"].astype(str).str.zfill(2) + df_final["code_com"].astype(str).str.zfill(3)
df_socio_eco['CODGEO'] = df_socio_eco['CODGEO'].astype(str).str.zfill(5)

print(df_socio_eco['CODGEO'].head())  # Voir les premières valeurs de CODGEO dans le fichier socio-économique
print(df_final['CODGEO'].head())  

# Vérifier la création de la colonne CODGEO dans df_final
print(df_final[["code_dept", "code_com", "CODGEO"]].head())

# Fusionner les deux fichiers sur la colonne 'CODGEO'
df_merged = pd.merge(df_final, df_socio_eco, on=['CODGEO', 'annee'], how='inner')


# Vérification du résultat
print(df_merged.head())

# Sauvegarder le fichier fusionné
df_merged.to_csv("fichier_final_fusionne.csv", index=False)
