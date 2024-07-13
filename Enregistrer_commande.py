from Charger_donnees import *
from sauvegarde_données import * 
from datetime import datetime
from Verification_saisies import *
from Verification_saisies import *
from colorama import Fore,Style
import time 

def enregistrer_commandes():
    liste_produits = charger_donnees_produit()
    
    nom_client = input("\t\t\tEntrez le nom du client : ")
    nom_produit = input("\t\t\tEntrez le nom du porduit : ")
    Quantite = input ("\t\t\tEntrez la quatité commandée ")
    date_livraison = input("\t\t\tEntrez la date de la livraison : ")
    compteur = 0 
    indice = 0 
    verificateur = commandes(nom_client,nom_produit,Quantite,date_livraison)
    verificateur_date = date_livre(date_livraison)
    if verificateur_date == 0:
        print(Fore.RED +"\n \t\t\tVous venez de saisir une mauvaise date de livraison"+Style.RESET_ALL)
        return
    else :
        if verificateur == 1:
            for produit in liste_produits: 
                if produit['NOM_PRODUIT'].lower() == nom_produit.lower() and produit['QUANTITE'] >= 0 and produit['QUANTITE'] >= int(Quantite)   :
                    compteur +=1  
            if compteur == 0:
                print(Fore.RED +" 🚨🚨 Le produit ne pas disponible ou bien la quantié est trop pour ce produit soit la quantité est inférieure à O"+Style.RESET_ALL)
            
            else: 
                liste_commande = charger_donnees_commande()
                if liste_commande == []:
                    indice = len(liste_commande)+1
                else :
                    indice = liste_commande[-1]['ID_COMMANDE']
                    indice = indice + 1

                heure = time.strftime('%H:%M:%S')   # permet de stocker l'heure à la quelle on ajoute la commande
                date = datetime.today().strftime('%d/%m/%Y') # permet de stocker la date à la quelle on la commande
            
                nouvelle_commande = {"ID_COMMANDE":indice,"NOM_CLIENT":nom_client,"NOM_PRODUIT":nom_produit,"QUANTITE":int(Quantite),"DATE_CMMD":date,"DATE_LVS":date_livraison,"HEURE":heure}
                liste_commande.nouvelle_commande
                sauvergade_donnees_commande(liste_commande)
                print(Fore.GREEN +"\n \t\t\t\tLa commande est bel bien enregistrée \n"+Style.RESET_ALL)
        else:
            return