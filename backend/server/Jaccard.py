import string

livre0 = "Harry Potter et le Prisonnier d'Azkaban"
livre1 = "Harry Potter et les Reliques de la Mort"
livre2 = "Jane Eyre"
livre3 = "Je suis Carla, c'est cool la vie, vie!"
livre4 = "Je suis giugiu, suis moi, bof cool!"
livre5 = "Harry Potter et le Prisonnier d'Azkaban"

auteur0 = "Carla Giuliani"
auteur1 = "J.K. Rowling"
auteur2 = "Emily Brontë"
auteur3 = "Charlotte Brontë"

all_livres={
    0: livre0,
    1: livre1,
    2: livre2,
    3: livre3,
    4: livre4,
    5: livre5
}

all_auteurs = {
    0: auteur0,
    1: auteur1,
    2: auteur2,
    3: auteur3
}

def transformText_to_Mots(livre):
    mots = (livre.lower()).split()
    liste =[]
    mots_finaux = []
    for mot in mots:
        if "'" in mot:
            liste = mot.split("'")
            mots.extend(liste)
            mots.remove(mot)

    for mot in mots:
        mot_nettoye = mot.strip(string.punctuation) 
        if len(mot_nettoye) >= 3 :  
            mots_finaux.append(mot_nettoye)

    return mots_finaux

def occurences_mots(mots):
    occurrences = {}
    for mot in mots :
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return occurrences


def distance_jaccard(l1,l2):
    l1_dico = occurences_mots(transformText_to_Mots(l1))
    l2_dico = occurences_mots(transformText_to_Mots(l2))
    # numerateur = Somme pour tt les mots => max(0,mot(l1)- mot(l2)) / max(mot(l1) , mot(l2))
    # denominatuer = nbr de mots différents
    numerateur = 0
    denominateur = len(l1_dico)
    for cle in l2_dico:
        if cle not in l1_dico: 
            denominateur +=1

    fl1 = 0
    fl2 = 0
    temp_num=0
    temp_deno = 0

    for cle, valeur in l1_dico.items():
        fl1 = valeur
        if cle in l2_dico:
            fl2 = l2_dico[cle]
        else:
            fl2= 0
        temp_num = max(0,fl2 - fl1)
        temp_deno= max(fl1,fl2)
        numerateur += temp_num / temp_deno

    for cle, valeur in l2_dico.items():
        fl2 = valeur 
        if cle not in l1_dico:
            fl1=0
            temp_num = max(0,fl2 - fl1)
            temp_deno= max(fl1,fl2)
            numerateur += temp_num / temp_deno
    
    return round(numerateur/denominateur, 3)


def graph_distance(livres,nb_livres):
    matrice=[]
    distance = 0
    i=0
    for i in range(nb_livres):
        ligne = []
        for j in range(nb_livres):
            if i==j : 
                ligne.append(0)
            else: 
                # OBLIGÉ de faire une sorte de tableau car "livre" + str(i) ne permet pas d'accéder à livre0
                l1 = all_livres[i]
                l2 = all_livres[j]
                distance = distance_jaccard(l1,l2)
                ligne.append(distance)
        matrice.append(ligne)

    return matrice

#def closeness_centrality(livre):  ou sinon => def betweeness_centrality(livre):
#    return 0


#ne donne pas les résultats attendus
def closeness_centrality(graph_distance, index):
    n = len(graph_distance)

    distance = sum(graph_distance[index])
    
    if distance != 0:
        valeur = (n - 1) / distance
    else:
        valeur = 0


    return valeur




distance_matrix = graph_distance(all_livres, 6)



    #Tmp en attendant de voir pour closeness ici on regarde juste les distances de jaccard
def plus_Proche(comparatif, all_livres):
    """    tmpL = []
    for i in all_livres:
        tmpL.append(distance_jaccard(requested_string, livre))
    return sorted(tmpL)"""
    ListNomDist = []
    for livre in all_livres.values():
        #la division sert à normaliser la distance pour limiter l'impact de la longueur de la String mais ça ne marche pas super bien
        ListNomDist.append((livre, distance_jaccard(comparatif, livre) / ((len(comparatif.split()) + len(livre.split())) / 2)))


    livres_tries = sorted(ListNomDist, key=lambda x: x[1])

    return livres_tries








requete = "Potter"
livres_tries = plus_Proche(requete, all_livres)

    




# TESTS #
# ----- #
#for book, distance in livres_tries:
#    print(f"Livre: {book}, Distance: {distance}")


#print(graph_distance(all_livres,6))
#print(distance_jaccard(livre0,livre1))
#print(occurences_mots(transformText_to_Mots(livre1)))