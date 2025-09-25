import plotly.express as px
import pandas as pd
# récupération avec panda du CSV
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')


figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

#création du camembert des ventes par produit 
figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')

figure.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')

#création du camembert du chiffre d'affaire par produit
données["total"] = données["prix"] * données["qte"]

figure = px.pie(données, values=données["total"], names='produit', title='chiffre d\'affaire par produit')

figure.write_html('chiffre-affaire-par-produit.html')

print('chiffre-affaire-par-produit.html généré avec succès !')
