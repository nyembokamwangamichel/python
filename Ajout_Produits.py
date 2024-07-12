import json
from Verification_saisies import * 
from colorama import Fore,Style
from Charger_donnees import * 
from sauvegarde_données import *
from datetime import datetime
import time 

# cette focntion permet  d'ajouter le produit
def ajouter_Produits(LISTE_PARAMETRE):
        DICTIONNAIRE_INTERMEDIAIRE = {"ID_PRODUIT":0,"NOM_PRODUIT":0,"PRIX_PRODUIT":0,"QUANTITE":0,"DATE":0,"HEURE":0} # Le dictionnaire qui va contenir les informations du nouveau produit avant de les inserer dans la liste LISTE_PARAMETRE
        if LISTE_PARAMETRE == []:
            id = len(LISTE_PARAMETRE)+1 # permet d'incrementer l'ID du produit à chaque enregistrement SA PRENDS LA TAILLE DU TABLEAU + 1
        else:
              id = LISTE_PARAMETRE[-1]['ID_PRODUIT']
              id = id + 1
        VERIFICATEUR  = 0  # permet de déclancher la boucle WHILE pour faire la vérification de saisie
        print(Fore.BLUE +"""\n \t\t\t\t ENREGISTREMENT DU PRODUIT\n"""+Style.RESET_ALL)
        while VERIFICATEUR < 2:

            if VERIFICATEUR == 1 :   # permet d'afficher autrement le messages après une erreur lors de la saisie des informations
                REP_UTILISATEUR = input("\t\tVOULEZ-VOUS QUITTER (QUITTER) OU BIEN MODIFIER (CONTINUE) ?: ")
                if REP_UTILISATEUR.lower() == "QUITTER".lower():  # permet d'arreter l'opération si l'utilisateur tape EXIT
                            print(Fore.RED +f"\n \t\t\t\tVOUS VENEZ D'ANNULER L'OPERATION  \n"+Style.RESET_ALL) 
                            return
                elif REP_UTILISATEUR.lower() == "CONTINUE".lower():   # permet de redémander à l'utilisateur les infos pour le produit
                    LISTE_PRODUITS = charger_donnees_produit()  # chargement du fichier PRODUIT.JSON et stocker les infos dans la variable LIESTE_PRODUITS
                    NOM_PRODUIT  = input("\t\tEntrez le nom du produit : ")
                    PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
                    QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")

                    VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)
                else:
                      VERIFICATEUR = 1
            else:
                LISTE_PRODUITS = charger_donnees_produit()  # chargement du fichier PRODUIT.JSON et stocker les infos dans la variable LIESTE_PRODUITS
                NOM_PRODUIT  = input("\t\tEntrez le nom du produit : ")
                PRIX_PRODUIT  = input("\t\tEntrez le prix du produit : ")
                QUANTITE_PRODUIT = input("\t\tEntrez la quantité du produit : ")

                VERIFICATEUR = verification_ajout_produit(NOM_PRODUIT,PRIX_PRODUIT,QUANTITE_PRODUIT,LISTE_PRODUITS,VERIFICATEUR,id)

        PRIX_PRODUIT = float(PRIX_PRODUIT)    # conversion du type de la valeur PRIX_PRODUIT en (FLOAT)
        # la partie qui permet d'ajouter les informations dans la liste intermediaire
        DICTIONNAIRE_INTERMEDIAIRE['ID_PRODUIT']=id
        DICTIONNAIRE_INTERMEDIAIRE['NOM_PRODUIT'] = NOM_PRODUIT
        DICTIONNAIRE_INTERMEDIAIRE['PRIX_PRODUIT']= PRIX_PRODUIT
        DICTIONNAIRE_INTERMEDIAIRE['QUANTITE']= int(QUANTITE_PRODUIT)
        heure = time.strftime('%H:%M:%S')   # permet de stocker l'heure à la quelle on ajoute le produit
        date = datetime.today().strftime('%d/%m/%Y') # permet de stocker la date à la quelle on ajoute le produit
        DICTIONNAIRE_INTERMEDIAIRE['DATE']= date
        DICTIONNAIRE_INTERMEDIAIRE['HEURE'] = heure 

        LISTE_PARAMETRE.append(DICTIONNAIRE_INTERMEDIAIRE)  # ajout de la liste intermediaire dans la liste parametre
        
        sauvergade_donnees_achat(LISTE_PARAMETRE)  # sauvegarde de la nouvelle liste qui contient l'element ajouter dans le fichier PRODUIT.JSON appartir de (la fonction sauvergade_donnees_achat) du module (sauvegarde_données)

        print(Fore.GREEN +"\n \t\t\t\tLe produit à été bien ajouter en stock \n"+Style.RESET_ALL)
        return LISTE_PARAMETRE


