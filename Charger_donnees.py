import json

# les fonction pour charger les information du fichier qui porte l'extension JSON qui jouent le rôle de BDD

def charger_donnees_produit():
    with open ('Produit.json','r') as FICHIER: 
         LISTE_PRODUITS = json.load(FICHIER)
         return LISTE_PRODUITS

def charger_donnees_vente():
    with open('rapport_vente.json','r') as FICHIER:
        LISTE_RAPPORT = json.load(FICHIER)
    return LISTE_RAPPORT

def charger_donnees_commande():
    with open('commendes.json','r') as FICHIER:
        LISTE_COMMANDE = json.load(FICHIER)
    return LISTE_COMMANDE

