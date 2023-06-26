import networkx as nx
import matplotlib.pyplot as plt

# Définition des nœuds du graphe
noeuds = ["Attente", "Montant insuffisant", "Montant suffisant", "Remboursement"]

# Définition des arêtes du graphe avec la valeur d'entrée et de sortie pour chaque arête
# Le tableau est composé de tableau eux même composé deux tuples.
# Le premier tuple correspond au noeud de départ et au noeud d'arrivé
# Le second tuple correspond à l'entrée et sortie de la connection. Ce second tuple est associé à une arrête
aretes = [
    [("Attente", "Montant insuffisant"), ("25", "OUTPUT_MESSAGE_INSUFFISANT")],
    [("Attente", "Montant suffisant"), ("50", "OUTPUT_MESSAGE_ATTENTE")],
    [("Attente", "Remboursement"), ("100", "OUTPUT_MESSAGE_REMBOURSEMENT")],
    [("Montant insuffisant", "Montant suffisant"), ("25", "OUTPUT_MESSAGE_ATTENTE")],
    [("Montant insuffisant", "Remboursement"), ("50", "OUTPUT_MESSAGE_REMBOURSEMENT")],
    [("Remboursement", "Montant suffisant"), ("OUTPUT_PIECE", "50")],
    [("Montant suffisant", "Attente"), ("SELECTION_CAFE", "OUTPUT_CAFE")]
]

def afficher_graphe(noeuds, aretes):
    # Création du graphe
    G = nx.DiGraph()

    # Ajout des nœuds au graphe
    G.add_nodes_from(noeuds)

    # Ajout des arêtes au graphe avec leurs attributs
    for arrete in aretes:
        depart, arrivee = arrete[0]
        entree, sortie = arrete[1]
        G.add_edge(depart, arrivee, entree=entree, sortie=sortie)

    # Configuration de l'affichage du graphe
    pos = nx.spring_layout(G, seed=42)  # Positionnement des nœuds
    edge_labels = {(u, v): d['entree'] + "/" + d['sortie'] for u, v, d in G.edges(data=True)}  # Étiquettes des arêtes

    # Affichage du graphe
    nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Affichage de la figure
    plt.title("Graphe")
    plt.axis('off')
    plt.show()

def parcourir_graphe(noeuds, aretes):
    resultats = []  # Liste pour stocker les résultats
    sequences = {}  # dict pour stocker les séquences
    indice_sequence = 1

    for noeud in noeuds:
        arretes_sortantes = []  # Liste pour stocker les arêtes sortantes du nœud sélectionné

        for arrete in aretes:
            depart, arrivee = arrete[0]

            if depart == noeud:  # Arête sortante du nœud sélectionné
                entree, sortie = arrete[1]
                arretes_sortantes.append((arrivee, entree, sortie))

        # Formatage et ajout du résultat pour les arêtes sortantes du nœud sélectionné
        resultats.append(f"Noeud sélectionné: {noeud}")
        for arrete_sortante in arretes_sortantes:
            arrivee, entree, sortie = arrete_sortante
            resultats.append(f"{noeud} -> {arrivee} : {entree}/{sortie}")

            # Recherche des arêtes sortantes des nœuds cibles
            for arrete in aretes:
                depart_cible, arrivee_cible = arrete[0]

                if depart_cible == arrivee: # and arrivee_cible != noeud:  # Arête sortante du nœud cible
                    entree_cible, sortie_cible = arrete[1]
                    resultats.append(f"\t\t{arrivee} -> {arrivee_cible} : {entree_cible}/{sortie_cible}")

                    # Ajout de la séquence à la liste
                    sequences[f"sequence {indice_sequence}"] = [entree, sortie, entree_cible, sortie_cible]
                    indice_sequence += 1

        resultats.append("")  # Ligne vide pour séparer les résultats des différents nœuds

    # Affichage des résultats
    print("\n".join(resultats))

    return sequences


def est_injection(entrees_sorties, sequence):
    # Vérifie si la séquence est une injection unique dans les entrées/sorties fournies
    for e, s in entrees_sorties:
        if e in sequence and s != sequence[e]:
            return False
    return True


def appliquer_uio(noeuds, aretes):
    sequences = {}  # Dictionnaire pour stocker les séquences
    entrees_sorties = []  # Liste pour stocker les entrées/sorties

    # Extraction des entrées/sorties
    for arrete in aretes:
        entree, sortie = arrete[1]
        entrees_sorties.append((entree, sortie))

    # Parcours du graphe pour trouver les séquences minimales
    for noeud in noeuds:
        for arrete in aretes:
            depart, arrivee = arrete[0]

            if depart == noeud:
                entree, sortie = arrete[1]

                for arrete_cible in aretes:
                    depart_cible, arrivee_cible = arrete_cible[0]

                    if depart_cible == arrivee: #and arrivee_cible != noeud:
                        entree_cible, sortie_cible = arrete_cible[1]
                        sequence = {entree: sortie, entree_cible: sortie_cible}

                        if est_injection(entrees_sorties, sequence):
                            sequences[f"Sequence {len(sequences) + 1}"] = sequence

    return sequences


# Appel de la fonction avec les nœuds et les arêtes donnés
sequences = parcourir_graphe(noeuds, aretes)
print("Liste des séquences:")
for cle, tableau in sequences.items():
    print(cle)
    print("\t- ".join(tableau))


# Appel de la fonction pour appliquer la méthode UIO
sequences = appliquer_uio(noeuds, aretes)

# Affichage des séquences minimales
print("Liste des séquences minimales:")
for cle, sequence in sequences.items():
    print(cle)
    for entree, sortie in sequence.items():
        print(f"\t- {entree} -> {sortie}")


def tester_couverture_complete(noeuds, aretes, sequences):
    chemins_couverts = set()  # Ensemble pour stocker les chemins couverts

    # Parcours du graphe en utilisant les séquences minimales
    for _, sequence in sequences.items():
        chemins = [sequence[entree] for entree in sequence.keys()]  # Liste des chemins dans la séquence

        # Parcours des chemins pour vérifier la couverture
        for i in range(len(chemins)):
            chemin = chemins[i]
            chemins_precedents = chemins[:i]  # Chemins précédents dans la séquence

            # Ajout des chemins précédents et du chemin actuel au chemin couvert
            chemin_couvert = tuple(chemins_precedents + [chemin])
            chemins_couverts.add(chemin_couvert)

    # Vérification de la couverture complète
    tous_les_chemins = set()
    for arrete in aretes:
        depart, arrivee = arrete[0]
        tous_les_chemins.add((depart, arrivee))

    couverture_complete = tous_les_chemins.issubset(chemins_couverts)

    return couverture_complete, chemins_couverts


# Appel de la fonction pour tester la couverture complète
couverture_complete, chemins_couverts = tester_couverture_complete(noeuds, aretes, sequences)

# Affichage des résultats
print("Couverture complète des chemins :", couverture_complete)
print("Chemins couverts :", chemins_couverts)



# Appel de la fonction avec les nœuds et les arêtes donnés
afficher_graphe(noeuds, aretes)
