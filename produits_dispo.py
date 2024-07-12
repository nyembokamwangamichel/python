import json 
from colorama import Fore,Style
from Charger_donnees import * 
#cette focntion permet d'afficher le produits disponibles
def Afficher_Produit_dispo(LISTE_PARAMETRE):
    
    LISTE_PARAMETRE = charger_donnees_produit()   # chargement du fichier PRODUIT.JSON

    print(Fore.BLUE +"\n \t\t\t\tLES PRODUITS DISPONIBLES \n"+Style.RESET_ALL)
    COMPTEUR = 0
    for PRODUIT in LISTE_PARAMETRE:
        if PRODUIT['QUANTITE'] > 0 :  # cette condition permet de verifier si la quantité de chaque produit a affiché est supperieure à 0
            COMPTEUR +=1
            print(f"\t\t ID : {PRODUIT['ID_PRODUIT']} | NOM PRODUIT : {PRODUIT['NOM_PRODUIT']}  | PRIX  : {PRODUIT['PRIX_PRODUIT']} | QUANTITE EN STOCK : {PRODUIT['QUANTITE']}")
            print("\t\t ================================================================================")
    if COMPTEUR == 0:
        print(Fore.RED+"\n \t\t\t\tLE STOCK EST VIDE\n"+Style.RESET_ALL)
    #     return COMPTEUR,LISTE_PARAMETRE
    # else:
    return COMPTEUR,LISTE_PARAMETRE