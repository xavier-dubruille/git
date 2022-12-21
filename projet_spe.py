from grille import Grille
from terrain_ennemi import Terrain_ennemi
from bateau import Bateau
import os


class Joueur:
    navires = {"Porte-avions": 5, "Croiseur": 4, "Contre-torpilleur": 3, "Sous-marin": 2}

    def __init__(self, nom):
        self.grille = Grille()
        self.terrain_ennemi = Terrain_ennemi()
        self.nom = nom
        self.flotte = []
        self.compteurj1 = 0
        self.compteurj2 = 0

    def placement_flotte(self):
        """PRE : deux inputs(chiffre entre 0 et 9) pour déterminer emplacement du bateau et un input pour sens bateau

           Si des mauvaises coordonnées sont introduites(hors map ou bateaux déja présent), recommence les inputs
           POST : ajoute un bateau dans le tableau flotte et affiche en console la position du bateau
           Affiche le retour de Ocean à savoir la grille des joueurs si l'appel a réussi.
           Permet le placement des bateaux si les méthodes de placement renvoient TRUE
           Si un problème de positionnement survient, l'utilisateur doit réencoder ses données.
           RAISE : ValueError si aucune données n'est introduite"""

        print("Choisissez une coordonnées entre 0 et 9 pour atribuer une ligne et une colonne à votre bateau ")
        print("Les bateux sont placés en partant de la droite et de haut en bas.")
        for bateau, taille in self.navires.items():

            drapeau = True
            while drapeau:
                self.apercu_ocean()
                try:
                    print("Veuillez placer votre %s" % (bateau))
                    ligne = int(input("Choisissez une ligne -----> "))
                    col = int(input("Choisissez une colonne -----> "))

                    while not 0 <= ligne <= 9 or not 0 <= col <= 9:
                        input("entrer des coordonnées valides")
                        ligne = int(input("Choisissez une ligne -----> "))
                        col = int(input("Choisissez une colonne -----> "))

                    orientation = str(
                        input("Verical ou horizontal (tapez v pour vertical ou h pour horizontal -----> "))
                    while orientation not in ["v", "V", "h", "H"]:
                        input("entrer une orientation valide")
                        orientation = str(
                            input("Verical ou horizontal (tapez v pour vertical ou h pour horizontal -----> "))

                    if orientation in ["v", "V"]:
                        if self.grille.placement_valide_ligne(ligne, col, taille):
                            self.grille.placement_bateau_ligne(ligne, col, taille)
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_vertical(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper "
                                  "la même case ou dépasser de la grille, réessayez!")

                    elif orientation in ["h", "H"]:
                        if self.grille.placement_valide_col(ligne, col, taille):
                            self.grille.placement_bateau_col(ligne, col, taille)
                            bateau = Bateau(bateau, taille)
                            bateau.positionnement_horizontal(ligne, col)
                            self.flotte.append(bateau)
                            drapeau = False
                        else:
                            input("Deux bateaux ne peuvent pas occuper la même case"
                                  "ou dépasser de la grille, réessayez!")

                    else:
                        continue

                    self.apercu_ocean()
                    input("appuyer sur une touche pour continuer")
                    os.system('cls')

                except ValueError:
                    print("Entrez un numéro...\n")

    def apercu_ocean(self):
        self.terrain_ennemi.aprecu_terrain_ennemi()
        print("|                 |")
        self.grille.apercu_grille()

    def coup_enregistre(self, ligne, col):
        """PRE : une ligne et une colonne en param pour une coordonée.
           POST : si la coo correspont à celle d'un bateau, l'enlève du tableau de coordonnées.
           Si bateau n'a plus de coo, le retire de la flotte et affiche message pour le dire."""

        for bateau in self.flotte:
            if (ligne, col) in bateau.coo:
                bateau.coo.remove((ligne, col))
                if bateau.verif_etat():
                    self.flotte.remove(bateau)
                    print("le %s de %s a été coulé!" % (bateau.modele, self.nom))

    def flotte_coule(self, joueur):
        """PRE : l'id de la personne à cibler(l'ordinateur(o) ou j1, j2)
           POST : renvoie True si en parcourant la grille, plus aucun bateau n'est présent.False si un B a été trouvé"""

        nbr_bateau = 0
        for grille_ligne in joueur.grille.grille:
            for case in grille_ligne:
                if case == "B":
                    nbr_bateau += 1
        if nbr_bateau == 0:
            return True
        else:
            return False

    def tir(self, cible):
        """PRE : l'id de la personne à cibler(l'ordinateur(o) ou j1, j2) puis deux inputs(chiffre entre 0 et 9) pour
           déterminer case à cibler. Si coordonnées déja ciblées ou inexistantes, répete le tir.
           POST : si un bateau adverse est touché, change la valeur de la case du tableau de tableau en X, O si raté
           Permet le tir si les méthodes de vérification renvoient TRUE.
           Raise : ValueError si aucune donnée n'est introduite"""

        self.apercu_ocean()
        try:
            print("\n%s Entrez les coordonnées à cibler..." % (self.nom))
            ligne = int(input("Choisissez une ligne -----> "))
            col = int(input("Choisissez une colonne -----> "))

            while not 0 <= ligne <= 9 or not 0 <= col <= 9:
                input("entrer des coordonnées valides")
                ligne = int(input("Choisissez une ligne -----> "))
                col = int(input("Choisissez une colonne -----> "))

            if self.grille.verif_ligne(ligne) and self.grille.verif_col(col):
                if cible.grille[ligne, col] == "B":
                    print("Touché!!!")
                    cible.grille[ligne, col] = "X"
                    cible.coup_enregistre(ligne, col)
                    self.terrain_ennemi[ligne, col] = "X"

                else:
                    if self.terrain_ennemi.terrain_ennemi[ligne][col] == "O" or \
                            self.terrain_ennemi.terrain_ennemi[ligne][col] == "X":
                        print("Coordonnées déjà ciblées....Regardez votre carte!")
                        self.tir(cible)
                    else:
                        print("Manqué...")
                        self.terrain_ennemi.terrain_ennemi[ligne][col] = "O"

            else:
                print("Ne visez pas le Lune, entrez des coordonnées valides...")
                self.tir(cible)

        except ValueError:
            print("Vous devez entrer des coordonnées....\n")
            self.tir(cible)

        input("Appuyez sur une touche")
        os.system('cls')