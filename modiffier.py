import json
from Verification_saisies import *
from Charger_donnees import *
from sauvegarde_données import * 
from colorama import Fore,Style
from datetime import datetime
import time 

def modification (COMPTEUR,RESULTAT):
  
    LISTE_MODIFICATION = charger_donnees_produit() # chargement du fichier produit

    print(Fore.BLUE +"\n \t\t\t\t ENTREZ LES NOUVELLES INFORMATIONS \n"""+Style.RESET_ALL)
    VERIFICATEUR = 0
    while VERIFICATEUR == 0:    
            NOM_PRODUIT  = input("\t\tEntrez le nom du produit : ")
            PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
            QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")
            
            VERIFICATEUR = verification_modification(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,VERIFICATEUR)   # verification de saisie
    
    LISTE_MODIFICATION[COMPTEUR-1]['NOM_PRODUIT'] = NOM_PRODUIT
    LISTE_MODIFICATION[COMPTEUR-1]['PRIX_PRODUIT'] = float(PRIX_PRODUIT)
    LISTE_MODIFICATION[COMPTEUR-1]['QUANTITE'] =  int(QUANTITE_PRODUIT)
    heure = time.strftime('%H:%M:%S')
    date = datetime.today().strftime('%d/%m/%Y')
    LISTE_MODIFICATION [COMPTEUR-1]['DATE'] = date
    LISTE_MODIFICATION [COMPTEUR-1] ['HEURE'] = heure 

    sauvergade_donnees_achat(LISTE_MODIFICATION)  # sauvegarde des infos pour le produit modifier

    print(Fore.GREEN +f"\n \t\t\t\tla modification du produit à été effectuée avec succès \n"+Style.RESET_ALL)