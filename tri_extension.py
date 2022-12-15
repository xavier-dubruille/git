import os
import time
import shutil

if __name__ == "__main__":

    choix = input('Voulez vous trier et imprimer (1) ou trier et placer dans fichier dédié(2)'
                  'ou trier dans l ordre décroissant(4) ou trier par taille(5). Afficher aide(3) : ')

    if choix == "":
        raise ValueError("aucune informations fournies")

    if choix == "1":

        chemin = input('Entrez le chemin absolu du dossier à trier :  ')

        if chemin == "":
            raise ValueError("aucune informations fournies")

        try:
            fichiers = os.listdir(chemin)
        except os.WindowsError:
            print("dossier introuvable")

        fichiers_tries = sorted(fichiers, key=lambda x: os.path.splitext(x)[1])
        for i in fichiers_tries:
            print(i)

    elif choix == "2":

        chemin = input('Entrez le chemin absolu vers le dossier ou aide si besoin d aide :  ')

        if chemin == "":
            raise ValueError("aucune informations fournies")

        if chemin in ["aide", "AIDE"]:
            print("donner un dossier à la fonction et elle triera chaque fichier par leur extension"
                  "et les placera dans un dossier créer spécialement pour les contenir")
            chemin = input('Entrez le chemin absolu vers le dossier ou aide si besoin d aide :  ')

        try:
            fichiers = os.listdir(chemin)
        except os.WindowsError:
            print("dossier introuvable")

        for i in fichiers:
            nom, extension = os.path.splitext(i)
            exension = extension[1:]

            if extension == "":
                continue

            if os.path.exists(chemin + '/' + extension):
                shutil.move(chemin + '/' + i, chemin + '/' + extension + '/' + i)

            else:
                os.makedirs(chemin + '/' + extension)
                shutil.move(chemin + '/' + i, chemin + '/' + extension + '/' + i)

    elif choix == "3":

        print("1 permet d'imprimer tous les fichiers par ordre alphabétique basé sur l'extension du fichier \n"
              "2 permet de trier les fichier et les diviser dans des dossiers créés si inexistant ou injecter \n"
              "si déja existant, les dossiers auront comme nomination l'extension des fichiers\n"
              "3 vous affichera un message d'aide si vous en avez besoin"
              "4 affiche l'heure et la date à laquelle ont été modifiés les fichiers"
              "5 pour trier sur base de la taille des fichiers")

    elif choix == "4":

        chemin = input('Entrez le chemin absolu du dossier à trier :  ')

        if chemin == "":
            raise ValueError("aucune informations fournies")

        try:
            fichiers = os.listdir(chemin)
        except os.WindowsError:
            print("dossier introuvable")

        fichiers_tries = sorted(fichiers, key=os.path.getmtime)

        for tri_date in fichiers_tries:
            try:
                str = time.strftime('%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(tri_date)))
                print(str, ' -->', tri_date)
            except OSError:
                print("fichier inexistant ou inateignable")

    elif choix == "5":
        chemin = input('Entrez le chemin absolu du dossier à trier :  ')

        if chemin == "":
            raise ValueError("aucune informations fournies")

        try:
            fichiers = os.listdir(chemin)
        except os.WindowsError:
            print("dossier introuvable")

        fichiers_tries = sorted(fichiers, key=lambda x: os.stat(x).st_size)

        for elem in fichiers_tries:
            try:
                tri_taille = os.stat(elem).st_size
                print(tri_taille, 'Ko -->', elem)
            except OSError:
                print("fichier inexistant ou inateignable")
