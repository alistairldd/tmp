# On instancie notre graphe de test ici
# Dans ce cas là c'est le graphe de l'exemple sur le sujet

N0 = [2,3,5,7]
N1 = [2,4,6,8]
N2 = [0,1,3,4,5,6]
N3 = [0,2,6]
N4 = [1,2,5]
N5 = [0,2,4]
N6 = [1,2,3]
N7 = [0]
N8 = [1]
G = [N0, N1, N2, N3, N4, N5, N6, N7, N8]


# Notre fonction principale ici qui contient des sous-fonctions. 
# C'est celle là que l'on va appeler pour faire nos tests
def coloration(k, graphe):
    # Initialisation
    n = len(graphe)
    color = [-1] * n
    # Fonction annexe pour vérifier si on peut colorer le noeud v avec la couleur c
    def is_safe(v, c):
        # On va vérifier pour tous les voisins du noeud si un d'entre eux est de couleur c
        for i in graphe[v]:
            if color[i] == c:
                # Si c'est le cas alors 2 noeuds adjacents ont la même couleur donc c'est pas bon
                return False
        return True
    
    def triDegre(graphe):
        degres = []
        # On parcourt tout le graphe en ajoutant dans notre liste de degrés un tuple (noeud, degré du noeud)
        # On dispose donc à présent d'une liste non triés de tuple
        for i in range(len(graphe)):
            degres.append((i, len(graphe[i])))
        # On utilise la fonction .sort() native de python, avec une fonction lambda permettant d'indiquer qu'on veut trier selon la deuxieme composante du tuple. 
        # Le reverse permet à notre résultat d'être décroissant
        degres.sort(key=lambda x: x[1], reverse=True)
        # Maintenant qu'on a notre liste de tuple trié, il nous suffit uniquement de renvoyer la liste des premiers indices (ceux des noeuds, sans les degrés)
        return [x[0] for x in degres]

    def coloriage2(graphe, color):
        # On trie les noeuds par ordre décroissant
        noeuds_tries = triDegre(graphe)
        
        # On parcourt les nœuds triés
        for v in noeuds_tries:
            # On essaye d'attribuer une couleur valide au nœud v
            for c in range(k):  # k est le nombre de couleurs disponibles
                if is_safe(v, c):
                    color[v] = c
                    break  # Passer au nœud suivant dès qu'une couleur est attribuée
        # Si tous les nœuds sont coloriés, retourner True
        return color

    

    
    def coloriage(m, color, v):
        # Cas de base, si on a atteint la taille du graphe c'est que la coloration est possible
        if v == n:
            return True 
        
        # On parcourt toutes les couleurs 
        for c in range (m):
            # On vérifie si la couleur c est valide pour colorier le noeud v en utilisant la fonction annexe is_safe, qui vérifie si un noeud peut être 
            #   colorié d'une certaine couleur
            if is_safe(v, c):
                # Si la couleur est safe pour le noeud v alors on instancie cette couleur dans notre tableau
                color[v] = c 
                # On appelle récursivement la fonction pour colorier le noeud suivant, si la coloration est possible alors on retourne True
                if coloriage(m, color, v+1):
                    return True 
                # Sinon on réinitialise la couleur du noeud v à -1 pour essayer une autre couleur
                color[v] = -1
        return False 
    
    
    
    # On appelle la fonction de coloriage pour le noeud 0, si elle retourne True alors le graphe est k-coloriable sinon il ne l'est pas
    if coloriage(k, color, 0):
        return color
    else :
        color = [-1] * n
        return coloriage2(graphe, color)
    
    
# On instancie le nombre de couleurs que l'on veut ici : 
nbCouleur = 3
res = coloration(nbCouleur, G)
print("Tentative de coloriage de graphe avec notre algorithme.")
print("On essaye de colorier le graphe G : ", G, "avec", nbCouleur, "couleurs") 
if -1 in res:
    print("Le graphe n'est pas coloriable, la liste des couleurs obtenue est : ", res) 
                
else:
    print("Le graphe est coloriable, voici la liste ddes couleurs résultat : ", res)
                
