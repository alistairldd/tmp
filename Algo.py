G = {
    "a" : ["b", "c"],
    "b" : ["a", "c", "d"],
    "c" : ["a", "b", "d", "e"],
    "d" : ["b", "c"],
    "e" : ["c", "f", "g"],
    "f" : ["e", "g"],
    "g" : ["e", "f"]
}


tab = [k for k in G.keys()] # Liste des sommets
cpt = 0 # Compteur pour attribuer les chiffres/couleurs
res = {} 
while len(res) < len(tab): #Tant qu'on a pas parcouru tous les sommets
    cpt += 1
    for x in tab:
        if x in res: # Si le sommet a déjà un chiffre, on passe au suivant
            continue
        else:
            trouve = True # On vérifie si tous nos voisins n'ont pas de chiffre en commun avec cpt
            for k in G[x]:
                if k in res and cpt == res[k]:
                    trouve = False
            if trouve:
                res[x] = cpt
print(res)
