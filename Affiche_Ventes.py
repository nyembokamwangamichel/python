import json
from colorama import Fore,Style
from Charger_donnees import *

#cette fonction permet d'afficher les ventes déjà effectuée
def afficher_vente():
    
    LISTE_VENTE = charger_donnees_vente() # permet de chargé le fichier vente.json en fin de recuperer les informations qu'y touvents et de l'effectées dans LISTE_VENTE
    print(Fore.BLUE +f"\n \t\t\t\tVENTES\n"+Style.RESET_ALL)
    COMPTEUR = 0   # La variable qui permet de vérifier si dans le fichier VENTE.json il y a des informations ou pas

    for VENTE in LISTE_VENTE:  # la boucle qui parcours le fichier ou bien la liste pour l'information des ventes et de les affichées
        COMPTEUR +=1
        print(f"ID VENTE {VENTE['ID']} |NOM CLIENT  {VENTE['Nom_client']} |PRODUIT {VENTE['Nom_produit']} | QUANTITE {VENTE['Quantite']} |PRIX UNITAIRE {VENTE['Prix_unitaire']} |PRIX A PAYER {VENTE['Prix_payer']} |DATE {VENTE['Date']} |HEURE {VENTE['Heure']}")
        print("========================================================================================================================================")
    if COMPTEUR == 0: # si le compteur est égal à 0 donc il n'a rien trouver dans le fichier
        print(Fore.RED +"\n \t\t\t\tIl y a aucunne vente effectuée\n"+Style.RESET_ALL)
    