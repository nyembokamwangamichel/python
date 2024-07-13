from colorama import Fore,Style
from afficher_commande import * 
from Enregistrer_commande import * 

def menu_princ():
    MENU = Fore.BLUE +"""\n """ +Style.RESET_ALL +"""
                        1.  Enregistrer une commande
                        2.  afficher les commandes
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
                            enregistrer_commandes()
                            return
                        elif CHOIX_UTILISATEUR =="2":
                            afficcher_commande()
                            return
                        elif CHOIX_UTILISATEUR == "3":
                            return  
