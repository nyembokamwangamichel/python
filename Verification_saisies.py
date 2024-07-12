from colorama import Fore,Style

# Cette fonction permet de verifier la saisie du module ajout_produit
def verification_ajout_produit(NOM_PRODUIT_PARAMETRE,PRIX_PRODUIT_PARAMETRE,QUANTITE_PRODUIT_PARAMETRE,LISTE_PRODUITS_PARAMETRE,VERIFICATEUR_PARAMETRE,ID_PARAMETRE):

    for PRODUIT in LISTE_PRODUITS_PARAMETRE: # permet de parcourir tout les elements du fichier produit
                # if VOIR_SI_VIDE > 0:
            if PRODUIT["NOM_PRODUIT"].lower() == NOM_PRODUIT_PARAMETRE.lower():    # vérifie si l'un de  touts les noms des produits qui sont le fichier produit est égal à ce qui est saisie par l'util
                print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 le produit que vous voulez ajouter est déjà dans le stock😯\n"+Style.RESET_ALL)
                VERIFICATEUR_PARAMETRE = 1
                return VERIFICATEUR_PARAMETRE 
            
    try:
        NOM_PRODUIT_PARAMETRE = int(NOM_PRODUIT_PARAMETRE)  # conversion du nom en entier / si oui donc c'est une mauvaise valeur sinon c'est une bonne
    except :            
            try : 
                PRIX_PRODUIT_PARAMETRE= float(PRIX_PRODUIT_PARAMETRE)   # conversion du prix en réel / si oui donc c'est une bonne valeur sinon c'est une mauvaise
                QUANTITE_PRODUIT_PARAMETRE = int(QUANTITE_PRODUIT_PARAMETRE)  #idem
            except : 
                    print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 il faut un entier pour  la quantité et le prix😯\n"+Style.RESET_ALL)
                    VERIFICATEUR_PARAMETRE = 1
                    return VERIFICATEUR_PARAMETRE
            else :
                    if NOM_PRODUIT_PARAMETRE == "" or PRIX_PRODUIT_PARAMETRE == "" or  QUANTITE_PRODUIT_PARAMETRE == "":
                            print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 touts les champs sont obligatoire😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS\n"+Style.RESET_ALL)
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    
                    elif  len(NOM_PRODUIT_PARAMETRE) < 3 : 
                            print(Fore.RED +f"\n \t\t\t\tMAUVAISE VALEUR POUR LE NOM DU PRODUIT🚨🚨 😯\n"+Style.RESET_ALL)
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    
                    elif float(PRIX_PRODUIT_PARAMETRE) <= 0 or  QUANTITE_PRODUIT_PARAMETRE <= 0:
                            print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯\n"+Style.RESET_ALL)
                            VERIFICATEUR_PARAMETRE = 1
                            return VERIFICATEUR_PARAMETRE
                    else:
                            VERIFICATEUR_PARAMETRE = 2 
                            return VERIFICATEUR_PARAMETRE
    else:
        print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 vous venez de saisir un entier pour le nom du produit😯\n \t\t\t\tVEUILLEZ SAISIR UNE CHAINE DE CARACTERES\n"+Style.RESET_ALL)
  
               
# cette focntion permet de  vérifier la saisie de vente
def verification_enregistrer_vente(NOM_CLIENT_PARAMETRE,NOM_PRODUIT_PARAMETRE,QUANTITE_VENDU_PARAMETRE,VERIFICATEUR_PARAMETRE):

        try:
                    NOM_CLIENT_PARAMETRE = int(NOM_CLIENT_PARAMETRE)   # conversion du nom client en entier / si oui donc c'est une mauvaise valeur sinon c'est une bonne
        except :   
                    try : 
                            QUANTITE_VENDU_PARAMETRE = int(QUANTITE_VENDU_PARAMETRE)   # conversion de la quantité vendu en entier / si oui donc c'est une bonne valeur sinon c'est une mauvaise
                    except : 
                            print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 il faut un entier pour  la quantité  😯\n"+Style.RESET_ALL)
                    else :
                            if NOM_CLIENT_PARAMETRE == "" or NOM_PRODUIT_PARAMETRE == "" or  QUANTITE_VENDU_PARAMETRE == "":
                                print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 touts les champs sont obligatoire  😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS \n"+Style.RESET_ALL)
                            elif  len(NOM_CLIENT_PARAMETRE) < 3 : 
                                print(Fore.RED +f"\n \t\t\t\tMauvaise valeur pour le nom du client 🚨🚨 😯\n \t\t\t\tLE NOM DU CLIENT DOIT CONTENIR 3 CARACTES MIN"+Style.RESET_ALL)
                            elif int(QUANTITE_VENDU_PARAMETRE) <= 0 :
                                    print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 le nombre min pour la quantité c'est 1 😯\n"+Style.RESET_ALL)
                            else:
                                    VERIFICATEUR_PARAMETRE = 1 
                                    return VERIFICATEUR_PARAMETRE
        else:
                print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 vous venez de saisir un entier pour nom DU CLIENT 😯\n \t\t\t\tVEUILLEZ SAISIR UNE CHAINE DE CARACTERES POUR CETTE CASE"+Style.RESET_ALL)
        return VERIFICATEUR_PARAMETRE

# cette fonction permet de vérifier la saisie de modification
def  verification_modification(NOM_PRODUIT_PARAMETRE,PRIX_PRODUIT_PARAMETRE,QUANTITE_PRODUIT_PARAMETRE,VERIFICATEUR_PARAMETRE):
            try:
                    NOM_PRODUIT_PARAMETRE = int(NOM_PRODUIT_PARAMETRE)  # conversion de nom du produit en entier / si oui donc c'est une mauvaise valeur sinon c'est une bonne
            except :
                try :
                    PRIX_PRODUIT_PARAMETRE = float(PRIX_PRODUIT_PARAMETRE)
                    QUANTITE_PRODUIT_PARAMETRE = int(QUANTITE_PRODUIT_PARAMETRE)
                except:
                        print(Fore.RED +f"\n \t\t\t\t Attention 🚨🚨 vous venez de saisir une chaine de caractères pour (la quantité ou prix unitaire)   😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR SAISIE LES ENTIERS POUR LES DEUX CASES\n"+Style.RESET_ALL)
                else:
                    if NOM_PRODUIT_PARAMETRE == "" or NOM_PRODUIT_PARAMETRE == "" or  QUANTITE_PRODUIT_PARAMETRE == "":
                        print(Fore.RED +f"\n \t\t\t\t Attention 🚨🚨 touts les champs sont obligatoire  😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS\n"+Style.RESET_ALL)
                    elif  len(NOM_PRODUIT_PARAMETRE) < 3 : 
                        print(Fore.RED +f"\n \t\t\t\tMAUVAISE VALEUR POUR LE NOM DU PRODUIT🚨🚨 😯\n"+Style.RESET_ALL)
                    elif PRIX_PRODUIT_PARAMETRE <= 0 or  QUANTITE_PRODUIT_PARAMETRE <= 0:
                        print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯\n"+Style.RESET_ALL)
                    else:
                        VERIFICATEUR_PARAMETRE = 1 
                        return  VERIFICATEUR_PARAMETRE 
            else:
                 print(Fore.RED +f"\n \t\t\t\t Attention 🚨🚨 Venez de saisir un entier pour le nom du produit 😯\n \t\t\t\tRASSIREZ-VOUS D'AVOIR ENTRER UNE CHAINE DE CARACTERES\n"+Style.RESET_ALL)
            return  VERIFICATEUR_PARAMETRE

# cette fonction permet de vérifier la saisie du module recherche produit
def recherche_produit(CHOIX_UTILISATEUR_PARAMETRE,VERIFICATEUR_PARAMETRE):
        if CHOIX_UTILISATEUR_PARAMETRE == "":
            print(Fore.RED +f"\n \t\t\t\tAttention  🚨🚨 le champs de nom du produit ne doit pas resté vide\n \t\t\t\t VEUILLEZ LE REMPLIR SVP  😯\n"+Style.RESET_ALL)
        else:
            VERIFICATEUR_PARAMETRE = 1
            return VERIFICATEUR_PARAMETRE
        return VERIFICATEUR_PARAMETRE

#cette focntion permet de vérifier la saisie du module VENTE
def verification_vente(REPONSE_UTILISATUER_PARAMETRE,VERIFICATEUR_PARAMETRE):
        if REPONSE_UTILISATUER_PARAMETRE =="":
            print(Fore.RED +f"\n \t\t\t\tAttention  🚨🚨 le champs pour le nom client est obligatoire\n \t\t\t\tVEUILLEZ LE REMPLIR SVP  😯\n"+Style.RESET_ALL)
        elif  REPONSE_UTILISATUER_PARAMETRE.isnumeric():
              print(Fore.RED +f"\n \t\t\t\tAttention 🚨🚨 rien que une chaîne de caracters qui est valide pour le nom d'un produit 😯\n"+Style.RESET_ALL)
        elif  len(REPONSE_UTILISATUER_PARAMETRE) < 3 : 
             print(Fore.RED +f"\n \t\t\t\tMAUVAISE VALEUR 🚨🚨 😯\n"+Style.RESET_ALL)
        else : 
             VERIFICATEUR_PARAMETRE = 1 
             return VERIFICATEUR_PARAMETRE
        
        return VERIFICATEUR_PARAMETRE