from Charger_donnees import *
from colorama import Fore,Style
from Verification_saisies import * 

# Cette focntion permet de cherger le vente par client
def vente_client ():
    
    LISTE_RAPPORT =  charger_donnees_vente()
    VERIFICATEUR  = 0
    while VERIFICATEUR == 0:
        REPONSE_UTILISATUER = input("\n \t\t\t\tEntrez le nom du client : ")
        VERIFICATEUR = verification_vente(REPONSE_UTILISATUER,VERIFICATEUR)
        
    COMPTEUR = 0
    print(Fore.BLUE +f"\n \t\t\t\tINFOS SUR LE(s) VENTE (S) EFFECTUEE (S) PAR {REPONSE_UTILISATUER} \n"+Style.RESET_ALL)
    for CLIENT in LISTE_RAPPORT:
            if CLIENT['Nom_client'].lower() == REPONSE_UTILISATUER.lower():
                COMPTEUR +=1
    print(Fore.BLUE+f"\n \t\t\t\t Nombre de ventes  éffectuer {COMPTEUR} vente (s) \n"+Style.RESET_ALL)
    for CLIENT in LISTE_RAPPORT:
            if CLIENT['Nom_client'].lower() == REPONSE_UTILISATUER.lower():
                COMPTEUR +=1
                print(f" ID VENTE : {CLIENT['ID']}  |NOM PRODUIT : {CLIENT['Nom_produit']} |QUANTITE : {CLIENT['Quantite']} |PRIX UNITAIRE : {CLIENT['Prix_unitaire']} |PRIX TOTAL A PAYER : {CLIENT['Prix_payer']} |DATE : {CLIENT['Date']} |HEURE : {CLIENT['Heure']}")
                print(" ===============================================================================================================================================")
    if COMPTEUR == 0: 
        print(Fore.RED +f"\n \t\t\t\tAucun client porte le nom  {REPONSE_UTILISATUER} 😯\n"+Style.RESET_ALL)
