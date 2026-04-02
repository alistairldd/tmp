
n1 = { 2 : 12,  3:10, 7:12}
n2 = {1:12, 3:8, 4:12}
n3 = {1:10, 2:8, 4:11, 5:3, 7:9}
n4 = {2:12, 3:11, 5:11, 6:10}
n5 = {3:3, 4:11, 6:6, 7:7}
n6 = {4:10, 5:6, 7:9}
n7 = {1:12, 3:9, 5:7, 6:9}


def SLPP():
    """ Méthode du sommet le plus proche"""


    n =[n1,n2,n3,n4,n5,n6,n7]

    r = n[0]
    visites = [1]
    distance =0
    # On parcourt tous les sommets non visités
    while len(visites) < len(n):
        # Variable trouve pour savoir si on a trouvé un sommet à ajouter
        trouve = False
        # On cherche le sommet le plus proche
        min = 100

        for i in r:
            if i not in visites:
                if r[i] < min:
                    min = r[i]
                    sommet = i
                    trouve = True

        # Y'a un problème si le sommet actuel n'a plus de chemin possible
        if trouve :
            # On ajoute le sommet à la liste des visites et on met à jour la distance
            visites.append(sommet)
            distance += min
        else : # Plus de chemin possible
            print("Il n'y a plus de chemin possible")
            break
        # On met à jour le sommet courant
        r = n[sommet-1]

    print ("Le chemin est : " + str(visites) + " et la distance totale est : " + str(distance))

    """

    La méthode SLPP n'est pas satisfaisante car si un sommet se retrouve avec tous ses voisins déjà visités, il n'y a plus de chemin possible pour continuer le cycle. 

    """

def CSIT1():
    """ Méthode CSIT-1 """
    n = [n1, n2, n3, n4, n5, n6, n7]

    # Initialisation
    r = n[0]
    visites = [1]  # Le cycle commence avec le premier sommet
    distance = 0

    # Trouver le sommet le plus proche du premier sommet
    min = 10000
    for i in r:
        if i != 1 and r[i] < min:
            min = r[i]
            sommet = i

    # Ajouter le sommet trouvé au cycle initial
    visites.append(sommet)
    distance += min

    # Ajouter le retour au premier sommet pour compléter la première tournée partielle
    distance += n[sommet - 1].get(1, float('inf'))  # Distance pour revenir au sommet initial
    visites.append(1)  # Retour au sommet initial
    print(f"Tournée partielle : {visites}, Distance : {distance}")

    # Appliquer la méthode CSIT-1 pour insérer les autres sommets
    while len(visites) < len(n) + 1:  # +1 car on inclut le retour au sommet initial
        meilleur_sommet = None
        meilleur_position = None
        min_augmentation = float('inf')

        # Parcourir tous les sommets non visités
        for i in range(1, len(n) + 1):
            if i not in visites:
                # Tester l'insertion dans chaque position du cycle
                for j in range(len(visites) - 1):  # Ne pas inclure le dernier sommet (retour au point de départ)
                    sommet_actuel = visites[j]
                    sommet_suivant = visites[(j + 1) % len(visites)]  # Modulo pour revenir au début du cycle

                    # Calculer l'augmentation de distance si on insère le sommet i
                    augmentation = (
                        n[sommet_actuel - 1].get(i, float('inf'))
                        + n[i - 1].get(sommet_suivant, float('inf'))
                        - n[sommet_actuel - 1].get(sommet_suivant, float('inf'))
                    )

                    # Trouver la meilleure insertion
                    if augmentation < min_augmentation:
                        min_augmentation = augmentation
                        meilleur_sommet = i
                        meilleur_position = j + 1

        # Insérer le sommet au meilleur endroit
        visites.insert(meilleur_position, meilleur_sommet)
        distance += min_augmentation
        print(f"Sommet inséré : {meilleur_sommet}, Position : {meilleur_position}, Distance ajoutée : {min_augmentation}")
        print(f"Visites : {visites}, Distance totale : {distance}")

    # Résultat final
    print("Le chemin est :", visites)
    print("La distance totale est :", distance)

SLPP()
CSIT1()