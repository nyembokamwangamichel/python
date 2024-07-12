
from produits_dispo import * 
from Verification_saisies import *
from sauvegarde_données import *
from Charger_donnees import *
from sauvegarde_données import * 
from datetime import datetime
import time 
from colorama import Fore,Style

# la fonction pour l'enregistrement de vente (s)

def Enregistrer_vente(LISTE_PRODUITS_PARAMETRE):
    LISTE_PRODUITS_RAPPORT = charger_donnees_vente()   # chargement du fichier RAPPORT_VENTE.JSON et on affecte ses elements dans la variable (liste) (LISTE_PRODUITS_RAPPORT)
    RESULTAT = {"ID":0,"Nom_client":0,"Nom_produit":0,"Quantite":0,"Prix_unitaire":0,"Prix_payer":0,"Date":0,"Heure":0}   # Dictionnaire vide qui contiendras les informations du nouveau vente / JOUE LE ROLE D'INTERMEDIAIRE
    COMPTEUR = 0  # la variable qui sert à compter les elements ou infos enregistrer dans le fichier RAPPORT_VENTE.JSON attraver la liste (LISTE_PRODUITS_PARAMETRE)
    VERIFICATEUR = 0  # permet de déclancher la boucle while pour passer à la vérification des infos saisies par l'utilisatuer
    ETAT_STOCK = 0   # vérifie si il y a les produits disponibles ou pas
    ETAT_STOCK,LISTE_PRODUITS_PARAMETRE = Afficher_Produit_dispo(LISTE_PRODUITS_PARAMETRE)   # permet de charger les produits dispos
    if ETAT_STOCK == 0:
        return 
    else: 
        while VERIFICATEUR == 0: 
            NOM_CLIENT  = input("\t\tEntrez le nom du client : ")
            NOM_PRODUIT = input("\t\tEntrez le nom du produit : ")
            QUANTITE_VENDU = input("\t\tEntrez la quantité : ")

            VERIFICATEUR =  verification_enregistrer_vente(NOM_CLIENT,NOM_PRODUIT,QUANTITE_VENDU,VERIFICATEUR)   # permet de faire la vérification de saisie grâce a la fonction verification_saisies...

        for PRODUIT in LISTE_PRODUITS_PARAMETRE:
   
            if  PRODUIT['NOM_PRODUIT'].lower() == NOM_PRODUIT.lower() and int(QUANTITE_VENDU) > 0   and int(PRODUIT['QUANTITE']) >= int(QUANTITE_VENDU) :  # Permet de verifier si le nom de produit vendu est bien dans la liste de produis dispos et si la quantité saisie par l'utilisateur ne pas superier a seul du produit ou un nombre négatif
                COMPTEUR +=1
                id = len(LISTE_PRODUITS_RAPPORT)+1  # incrementation de l'ID
                heure = time.strftime('%H:%M:%S')  # recuperation de l'heure atuelle
                date = datetime.today().strftime('%d/%m/%Y')  # recuperation de la date atuelle
                # stockage des informations dans la liste RESULTAT
                PRIX_TOTAL_A_PAYER = float(int(QUANTITE_VENDU)* PRODUIT['PRIX_PRODUIT'])
                RESULTAT['ID']=(id)
                RESULTAT['Nom_client']=(NOM_CLIENT.capitalize())
                RESULTAT['Nom_produit']= NOM_PRODUIT
                RESULTAT['Quantite']=int(QUANTITE_VENDU)
                RESULTAT['Prix_unitaire']= (PRODUIT['PRIX_PRODUIT'])
                RESULTAT['Prix_payer'] =(PRIX_TOTAL_A_PAYER)
                RESULTAT['Date']=(date)
                RESULTAT['Heure']=(heure)
                PRODUIT['QUANTITE']=(PRODUIT['QUANTITE'] - int(QUANTITE_VENDU))

                LISTE_PRODUITS_RAPPORT.append(RESULTAT)
                sauvergade_donnees_vente(LISTE_PRODUITS_RAPPORT)   # Permet d'enregistrer les nouvelles infos pour vente
                sauvergade_donnees_achat(LISTE_PRODUITS_PARAMETRE)  # permet d'enregistrer les nouvelles infos pour produit
                print(Fore.GREEN +"\n \t\t\t\tL'évément a été bien enregistré\n"+Style.RESET_ALL)
                # sauvegarder_rapport(RESULTAT)
        if COMPTEUR == 0:
            print(Fore.RED +"\n \t\t\t\techec de vente 🚨 soit :\n \t\t\t\tle produit ne pas disponible,\n \t\t\t\tla quantité vendu est supérieure à la Quantité en stock pour ce produit. "+Style.RESET_ALL)
        


# def somme(nbr1,Nbre2):
#     somm = nbr1+Nbre2
#     return somm,9
# som,p = somme(2,4)

# print(som,p)