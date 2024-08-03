import csv
from Charger_donnees import *
from colorama import Fore,Style

def exportation():
    tableau = ['ID','Nom_client','Nom_produit','Quantite','Prix_unitaire','Prix_payer','Date','Heure','\n']
    liste_rapport = charger_donnees_vente()
    if liste_rapport == []:
         print(Fore.RED +"\n \t\t\til aucun rapport etabli pour la vente "+Style.RESET_ALL)
         return
    else:

        LISTE_INTER = []
        liste =[]
        for rapport in liste_rapport:
            for infos in rapport.values():
                infos = str(infos)
                liste.append(infos)
        LISTE_INTER.append(liste)

        with open('Rapport.csv','w+') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(tableau)
            writer.writerows(LISTE_INTER)
        print(Fore.GREEN +"\n \t\t\tExportation du rapport términer"+Style.RESET_ALL)


    


