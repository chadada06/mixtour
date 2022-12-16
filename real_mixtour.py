# on importe la fonction que l'on va utiliser pour tirer au sort le joueur_qui_commence
from random import randint
from colorama import Back, Fore, init  # on importe le module colorama
init(autoreset=True)  # va nous permettre de colorer un fond et un texte


 

def afficher_stock():
    """
    fonction qui ne prends rien en parametre,
    sans return car qui va uniquement servir a l'affichage
    va afficher le stock des points
    """
    print(Fore.RED+("Les rouges ont"+str(stock_rouge)))
    print(Fore.BLUE+("Les bleus ont"+str(stock_bleu)))


def points():
    """
    fonction qui ne prends rien en parametre,
    sans return car qui va uniquement servir a l'affichage
    va afficher le score des joueurs
    """
    print(Fore.RED+"Score rouge:"+str(score_rouge),
          Fore.BLUE+"  Score bleu:"+str(score_bleu))


mon_plateau = {
    "A": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    "B": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    "C": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    "D": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
    "E": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
}


def affichage_de_plateau(pl):  # la fonction sert à afficher le plateau
    print("      ",end="")#on affiche le plateau 
    for n in range (1,6):
        print("   ",n,"  ", end="")
    print("\n", end="")
    choix = 1
    for I in pl.keys():
        print("  ", I, "  ", end="")
        for j in range(5):
            if j % 2 == choix:
                print(Back.BLACK+affichage_case(I, j), end="")
            else:
                print(Back.WHITE+affichage_case(I, j), end="")
        print("\n", end="")
        choix = (choix+1) % 2


def affichage_case(ligne, colone):  # la fonction sert à afficher les cases avec les points
    result = ""
    case = mon_plateau[ligne][colone]
    for i in case:
        if i == 0:
            c = " "
        elif i == 1:
            c = Fore.RED+"R"
        else:
            c = Fore.BLUE+"B"
        result = result+c
    return result


def demander_nouveau_reset(pl):
    print("ce déplacement est interdit.")
    choice = input(
        "Entrer de nouveau la case de la pile à deplace (d)\nRevenir au choix ajouter/deplacer (r)")
    if choice == 'd':
        return deplacer(pl)
    elif choice == 'r':
        return 'reset'
    else:
        return demander_nouveau_reset(pl)


def verifier_deplacement(pl,case_pile_deplacer):
    case_ou_deplacer=input("où voulez vous déplacer cette pile ?")
    # verifi que la case existe
    if case_ou_deplacer[0] not in pl.keys() or int(case_ou_deplacer[1]) not in range(1, 6):
        print("cette case n'existe pas.")
        return verifier_deplacement(pl,case_pile_deplacer)
    elif case_ou_deplacer==case_pile_deplacer:#verifi si le déplacement est autorisé
        return demander_nouveau_reset(pl)
    else:
        collone_source = int(case_pile_deplacer[1])
        collone_destination = int(case_ou_deplacer[1])
        ligne_source = ord(case_pile_deplacer[0])
        ligne_destination = ord(case_ou_deplacer[0])
        for x in range(collone_source-1,collone_source+2) :
            for y in range (ligne_source-1,ligne_source+2):
                if ligne_destination==y and collone_destination==x:
                    return case_ou_deplacer
        return demander_nouveau_reset(pl)

def demander_nombre_pions(taille_pile):
    nombre_pion_pile_deplacer=input("combien de pions de la pile voulez vous déplacer? ")
    try:
        nb_pions = int(nombre_pion_pile_deplacer)
    except ValueError:
        print("il faut entrer un nombre entier.")
        return demander_nombre_pions(taille_pile)
    if nb_pions>taille_pile:#verifi si le nombre de pions à déplcer est valide
        print("il n'y a pas assez de pions dans cette pile.")
        return demander_nombre_pions(taille_pile)
    else:
        return nb_pions

def taille_de_pile(case_x,pl):
    result=0
    for nb in pl[case_x[0]][int(case_x[1])-1]:#calcul de la taille de la pile 
        if nb!=0:
            result+=1
        else:
            break
    return result

def deplacer_pile(pl,taille_pile,case_pile_deplacer,case_ou_deplacer,nombre_pion_pile_deplacer):
    pions=[]
    index=taille_pile-1
    while True:
        pions.append(pl[case_pile_deplacer[0]][int(case_pile_deplacer[1])-1][index])#on supprime les pions à déplacer de la case initiale
        pl[case_pile_deplacer[0]][int(case_pile_deplacer[1])-1][index]=0
        index-=1
        if index<taille_pile-nombre_pion_pile_deplacer:
            break
    pions.reverse()
    taille_pile_destination = taille_de_pile(case_ou_deplacer,pl)
    for i in range(len(pions)):#on ajoute à la case finale les pions à déplacer
        pl[case_ou_deplacer[0]][int(case_ou_deplacer[1])-1][i+taille_pile_destination]=pions[i]

def deplacer(pl):
    """
    déplace une pile 
    prend pour agrument un dictionnaire

    """
    case_pile_deplacer=input("dans quelle case se trouve la pile que souhaitez vous déplacer?")
    if case_pile_deplacer[0] not in pl.keys() or (int(case_pile_deplacer[1])<1 or int(case_pile_deplacer[1])>5):#vérifi si la case existe
        print("cette case n'existe pas.")
        return deplacer(pl)
    else:
        if pl[case_pile_deplacer[0]][int(case_pile_deplacer[1])-1][0]==0:#verifi s'il y a une pile dans la case
            print("cette case est vide.")
            return deplacer(pl)
        else:
            result = verifier_deplacement(pl,case_pile_deplacer)
            if result != 'reset':
                taille_pile=taille_de_pile(case_pile_deplacer,pl)
                nb_pions = demander_nombre_pions(taille_pile)
                deplacer_pile(pl,taille_pile,case_pile_deplacer,result,nb_pions)
            else:
                return result
            

def ajouter(pl):
    global stock_bleu,stock_rouge
    case_pion_ajouter=input("dans quelle case se trouve la pile que souhaitez vous ajouetr un pion?")
    if case_pion_ajouter[0] not in pl.keys() or (int(case_pion_ajouter[1])<1 or int(case_pion_ajouter[1])>5):#vérifi si la case existe
        print("cette case n'existe pas.")
        return ajouter(pl)
    else:
        if pl[case_pion_ajouter[0]][int(case_pion_ajouter[1])-1][0]!=0:#verifi s'il y a une pile dans la case
            print("cette case est pleine, il faut choisir une case vide.")
            return ajouter(pl)
        else:
            if premier_joueur_tour==1:
                pl[case_pion_ajouter[0]][int(case_pion_ajouter[1])-1][0]=2
                stock_bleu=stock_bleu-1
            else:
                pl[case_pion_ajouter[0]][int(case_pion_ajouter[1])-1][0]=1
                stock_rouge=stock_rouge-1
                

def gagner(plateau,stock_blue,stock_red,score_blue,score_red,column,row):
    for i in plateau[row][column]:

        if len(plateau[row][column][i]==5):
            #blue 1, red 0
            if plateau[row][column][-1]==1:#ATTENTION CE NE SER PAS TJR LE DERNIERESPACE DE LA CASE 
                score_blue+=1
                stock_blue+=5#ATTENTION IL FAUT AJOUTER AU STOCK LES PIONS BLEUS DE LA PIE QUI N4EST FORCEMENT CONSTITUEE QUE DE BLEU
                plateau[row][column] = [0,0,0,0,0]#IL N'Y A PAS FORCEMENT QUE 5 PIONSDANS LA PILE GAGNANTE 
            else:
                score_red+=1
                stock_red+=5#ATTENTION IL FAUT AJOUTER AU STOCK LES PIONS ROUGES DE LA PIE QUI N4EST FORCEMENT CONSTITUEE QUE DE ROUGE
                plateau[row][column] = [0,0,0,0,0]#IL N'Y A PAS FORCEMENT QUE 5 PIONSDANS LA PILE GAGNANTE

    return score_red, stock_blue, score_red, score_blue

affichage_de_plateau(mon_plateau)

nom_bleu=input("Quel est le nom du joueur bleu? ") #on demande les noms des joueurs et on leur associe une couleur
nom_rouge=input("Quel est le nom du joueur rouge? ")
print(Fore.BLUE+("Le joueur bleu est "+nom_bleu))
print(Fore.RED+("Le joueur rouge est "+nom_rouge))

joueur_qui_commence=randint(0,1) #on va prendre le joueur qui commence au hasard 
if joueur_qui_commence==1: #en associant un nombre tire au hasard a chaque couleur
    premier_joueur_tour=1 #on va utiliser cette variable pour dire qui commence puis alterner le premier joueur a chaque tour
else :
    premier_joueur_tour=0

stock_rouge=25 #on initialise les stocks a 25
stock_bleu=25
score_rouge=0 #on initialise les scores a 0
score_bleu=0


while score_bleu<5 or score_rouge<5:
    phrase = Fore.BLUE+("C'est au tour de "+nom_bleu+" de jouer.") if (premier_joueur_tour == 1) else  Fore.RED+("C'est au tour de "+nom_rouge+" de jouer.")
    print(phrase)
    choix=input("Voulez vous ajouter un nouveau pion (a) ou deplacer une pile (d) ? ")
    points()
    if choix=="a":
        ajouter(mon_plateau)
        affichage_de_plateau(mon_plateau)
    elif choix=="d":
        choice = deplacer(mon_plateau)
        if choice == 'reset':
            continue
        affichage_de_plateau(mon_plateau)
    else:
        print("Vous devez entrer (a) si vous souhaiter ajouter un nouveau pion ou (d) si vous souhaitez deplacer une pile.")
        
    premier_joueur_tour=(premier_joueur_tour+1)%2 #on va alterner a chaque fois entre 1 et 0 pour changer le premier joueur dans le tour
    afficher_stock()

if score_bleu==5 or score_rouge==5:
    if score_bleu==5:
        print(Fore.BLUE+("Cest fini, le gagnant est "+nom_bleu))
    else:
        print(Fore.RED+("Cest fini, le gagnant est "+nom_rouge))