from Charger_donnees import *
from colorama import Fore,Style

def afficcher_commande():
    liste_commande = charger_donnees_commande()
    if liste_commande == []:
        print(Fore.RED +"\n \t\t\t\tIl y a aucunne commande\n"+Style.RESET_ALL)
        return
    
    else: 
        for commande in liste_commande:
            print(f"ID : {commande['ID_COMMANDE']} | NOM_CLIENT : {commande['NOM_CLIENT']} | NOM_PRODUIT: {commande['NOM_PRODUIT']} | QUANTITE : {commande['QUANTITE']} | DATE_COMMANDE : {commande['DATE_CMMD']} | DATE_LIVRAISON : {commande['DATE_LVS']} | HEURE : {commande['HEURE']}")
   