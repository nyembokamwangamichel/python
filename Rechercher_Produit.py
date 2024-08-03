import json 
from colorama import Fore,Style
from Verification_saisies import *
from Charger_donnees import *
from suppression_prduit import * 
from modiffier import * 

# la focntion  pour la recherche d'un produit
def rechercher_produit():

    LISTE_PRODUIT = charger_donnees_produit()  # chargement fichier produit
    
    RESULTAT = []  # liste vide pour stocker les produit trouver
    COMPTEUR = 0
    VERIFICATEUR = 0

    # while VERIFICATEUR == 0: 
    Menu_choix = input("\n \t\t\t\t1. Rechercher par nom\n \t\t\t\t2. Rechercher par ID\n \t\t\t\tVotre choix :")
        # VERIFICATEUR = recherche_produit (CHOIX_UTILISATEUR,VERIFICATEUR)   # verification de saisie

    if Menu_choix == "1":
        nom = input("\n \t\t\t\tEntrez le du client : ")
        for PRODUIT in LISTE_PRODUIT:  # permet de parcourir le produit
            if PRODUIT['NOM_PRODUIT'].lower() == nom.lower():   # pour comparer le nom du produit qui est saisi par l'utilisateur au nom de tout les produits pour trouver seul qui est égal
                COMPTEUR +=1
                RESULTAT.append(PRODUIT)
        if COMPTEUR == 0:
            print(Fore.RED +f"\n \t\t\t\tAucun produit porte le nom  {nom} 😯\n"+Style.RESET_ALL)
            return
        else:
            print (Fore.BLUE +f"\n \t\t\t\tLE PRODUIT A ETE TROUVE\n"+Style.RESET_ALL)
            
            for PRODIT_DISP in RESULTAT:
                print(f"\t\tID : {PRODIT_DISP['ID_PRODUIT']} | NOM PRODUIT : {PRODIT_DISP['NOM_PRODUIT']} | PRIX : {PRODIT_DISP['PRIX_PRODUIT']} | QUANTITE EN STOCK :  {PRODIT_DISP['QUANTITE']}")
                print("\t\t================================================================================")

    elif Menu_choix == "2": 
        id_pro = input("\n \t\t\t\tEntrez l'ID : ")
        for PRODUIT in LISTE_PRODUIT:  # permet de parcourir le produit
            if str(PRODUIT['ID_PRODUIT']) == id_pro:   # pour comparer le nom du produit qui est saisi par l'utilisateur au nom de tout les produits pour trouver seul qui est égal
                COMPTEUR +=1
                RESULTAT.append(PRODUIT)
        if COMPTEUR == 0:
            print(Fore.RED +f"\n \t\t\t\tAucun produit porte l'ID  {id_pro} 😯\n"+Style.RESET_ALL)
            return
        else:
            print (Fore.BLUE +f"\n \t\t\t\tLE PRODUIT A ETE TROUVE\n"+Style.RESET_ALL)
            
            for PRODIT_DISP in RESULTAT:
                print(f"\t\tID : {PRODIT_DISP['ID_PRODUIT']} | NOM PRODUIT : {PRODIT_DISP['NOM_PRODUIT']} | PRIX : {PRODIT_DISP['PRIX_PRODUIT']} | QUANTITE EN STOCK :  {PRODIT_DISP['QUANTITE']}")
                print("\t\t================================================================================")
    elif Menu_choix != "1" or Menu_choix != "2":
        print(Fore.RED +"\n \t\t\t\tMauvais choix"+Style.RESET_ALL)
        return
    
    MENU = Fore.BLUE +"""\n """ +Style.RESET_ALL +"""
                        1.  supprimer le produit
                        2.  modifier
                        3.  Quitter
                        ❓ Votre choix : """

    MENU_CHOICES = ["1","2","3"]   # la liste MENU_CHOIX contient les différents choix selon le menus dispo


    while True:    
                        CHOIX_UTILISATEUR = "" # la variable qui contiendrans le choix de l'utilisateurs pour les menus
                        while CHOIX_UTILISATEUR not in MENU_CHOICES: # la boucle qui turne si le choix taper par l'utilisateur ne pas dans la liste de choix
                            CHOIX_UTILISATEUR = input(MENU)
                            if CHOIX_UTILISATEUR not in MENU_CHOICES:
                                print(Fore.RED +"\t\tVeuillez Choisir une option valide..."+Style.RESET_ALL)
                        if CHOIX_UTILISATEUR == "1":  # toutes les structures , permettentes de lancer un fonction précise selon le choix
                            suppr_produit(COMPTEUR)
                            return
                        elif CHOIX_UTILISATEUR =="2":
                            modification(COMPTEUR,RESULTAT)
                            return
                        elif CHOIX_UTILISATEUR == "3":
                            return  # une fonction de python importée depuis le module sys, qui permet d'arreter l'execution du code
