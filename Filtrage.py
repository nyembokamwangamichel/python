from colorama import Fore,Style
from Charger_donnees import *


def filtrage():
    fichiers_vente = charger_donnees_vente()

    print(Fore.BLUE +"""\n \t\t\t\t FILTRAGE\n"""+Style.RESET_ALL)
    if fichiers_vente == []:
           print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 il y a aucune vente enregistrée\n"+Style.RESET_ALL)
           return
    else :       
        date_debut = input("\n \t\tEntrez la date de debut DD-MM-YYYY : ")
        date_fin = input("\n \t\tEntrez la date de la fin DD-MM-YYYY : ")
        if date_debut == "" or date_fin == "":
            print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 touts les champs sont obligatoire😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS\n"+Style.RESET_ALL)
            return
        else:
            LISTE_FILTRE = []
            COMPTERUR = 0
            for VENTE  in fichiers_vente :
                if VENTE['Date'] >=  date_debut and VENTE['Date'] <= date_fin :
                    COMPTERUR +=1
                    LISTE_FILTRE.append(VENTE)
                else :
                    continue
            if COMPTERUR == 0 : 
                print(Fore.RED +f"\n \t\t\tIl y a aucunne vente à été éffectué avec entre {date_debut} et {date_fin}"+Style.RESET_ALL)
            else:
                print(Fore.GREEN +"\n \t\t\t\tles ventes filtrées \n"+Style.RESET_ALL)
                for VENTE in LISTE_FILTRE:
                    print(f"ID VENTE {VENTE['ID']} |NOM CLIENT  {VENTE['Nom_client']} |PRODUIT {VENTE['Nom_produit']} | QUANTITE {VENTE['Quantite']} |PRIX UNITAIRE {VENTE['Prix_unitaire']} |PRIX A PAYER {VENTE['Prix_payer']} |DATE {VENTE['Date']} |HEURE {VENTE['Heure']}")

    

