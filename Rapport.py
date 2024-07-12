from datetime import datetime
from colorama import Fore,Style
from Charger_donnees import *
import json

#Cette focntion permet a générer un rapport journalier pour tout activité
def rapport ():

    LISTE_VENTE = charger_donnees_vente()

    # COMPTEUR = 0
    COMPTEUR2 = 0
    COMPTEUR3 = 0
    date = datetime.today().strftime('%d/%m/%Y')

    print(Fore.BLUE +"\n \t\t\t\tRAPPORT JOURNALIER:"+Style.RESET_ALL)

    print(Fore.BLUE +"\n \t\t\t\tVENTES \n"+Style.RESET_ALL)
          
    for VENTE in LISTE_VENTE:   # parcours le fichier pour les VENTES
            COMPTEUR2 +=1
            print(f"ID VENTE {VENTE['ID']} |NOM CLIENT {VENTE['Nom_client']} |NOM PRODUIT {VENTE['Nom_produit']} |QUANTITE {VENTE['Quantite']} |PRIX UNITAIRE {VENTE['Prix_unitaire']} |PRIX TOTAL A PAYER {VENTE['Prix_payer']} |DATE {VENTE['Date']} |HEURE {VENTE['Heure']}")
            print("===========================================================================================================================================================")
    if COMPTEUR2 == 0:
         print(Fore.RED +"\n \t\t\t\tAUCUNNE VENTE A ETE FAITE AUJOURD'HUI\n")