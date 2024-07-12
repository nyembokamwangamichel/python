from Charger_donnees import * 
from sauvegarde_données import *
from colorama import Fore,Style

def suppr_produit (POSITION):
    LISTE_PRODUITS = charger_donnees_produit()
    # INFO_ELEMENT_SUP = {"ID_PRO":0}
    # INFO_ELEMENT_SUP['ID_PRO'] = LISTE_PRODUITS[POSITION['ID_PRODUIT']]
    del LISTE_PRODUITS[POSITION-1]
    print(Fore.GREEN+"`\t\t\tle produit est supprimer"+Style.RESET_ALL)
    sauvergade_donnees_achat (LISTE_PRODUITS)
    