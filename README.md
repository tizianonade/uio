> La méthode unique input output (UIO) est utilisée pour trouver des séquences de tests minimales pour un graphe. 
> Elle permet de garantir que chaque combinaison d'entrées possibles est testée au moins une fois.

Dans votre code, vous avez déjà implémenté une fonction parcourir_graphe qui génère les séquences en utilisant l'algorithme UIO. 
Les séquences sont stockées dans le dictionnaire sequences.

Pour afficher les séquences, vous pouvez ajouter le code suivant à la fin de votre script :
La méthode UIO (Unique Input Output) nécessite une implémentation spécifique pour extraire les séquences minimales du graphe. 
Voici une modification de votre code qui applique la méthode UIO et génère les séquences minimales :


Dans cette modification, 
la fonction appliquer_uio utilise une fonction auxiliaire est_injection 
pour vérifier si une séquence est une injection unique dans les entrées/sorties fournies. 
La fonction appliquer_uio parcourt le graphe en utilisant les nœuds et les arêtes pour trouver les séquences minimales 
qui satisfont les critères de l'algorithme UIO. 
Les séquences minimales sont stockées dans le dictionnaire sequences et affichées à la fin du script.

N'oubliez pas d'exécuter la fonction appliquer_uio 
après avoir défini les nœuds et les arêtes, et avant d'afficher les séquences minimales.

Pour interpréter les résultats obtenus à partir de l'application de la méthode UIO, vous pouvez suivre les étapes suivantes :

Liste des séquences minimales : 
La première ligne affiche "Liste des séquences minimales:". 
En dessous de cette ligne, chaque séquence minimale est affichée avec un numéro d'identification (par exemple, "Sequence 1", "Sequence 2", etc.).

Pour chaque séquence minimale : 
Chaque séquence minimale est affichée avec les paires d'entrées et de sorties correspondantes. 
Par exemple, pour la séquence minimale "Sequence 1", 
les paires d'entrées et de sorties sont affichées sous la forme "- [entrée] -> [sortie]".

Par exemple :
Sequence 1
- 25 -> OUTPUT_MESSAGE_INSUFFISANT
- 50 -> OUTPUT_MESSAGE_ATTENTE
- 100 -> OUTPUT_MESSAGE_REMBOURSEMENT

Cela signifie que pour la première séquence minimale, 
vous devez tester les entrées suivantes avec les sorties correspondantes : 
25 avec "OUTPUT_MESSAGE_INSUFFISANT", 
50 avec "OUTPUT_MESSAGE_ATTENTE", 
et 100 avec "OUTPUT_MESSAGE_REMBOURSEMENT".

Interprétation des séquences : 
Les séquences minimales vous donnent les combinaisons spécifiques d'entrées et de sorties à tester 
pour garantir une couverture complète des chemins dans votre graphe. 
Vous pouvez utiliser ces séquences pour effectuer des tests et 
vérifier si votre système réagit correctement aux différentes combinaisons d'entrées.

Par exemple, vous pouvez utiliser les séquences minimales 
pour vérifier si votre système génère les bonnes sorties en réponse à des entrées spécifiques. 
Vous pouvez également utiliser ces séquences pour identifier 
d'éventuels problèmes ou erreurs dans votre système en vérifiant si toutes les combinaisons possibles sont correctement traitées.

Assurez-vous de tester chaque séquence minimale et d'observer les sorties générées par votre système pour valider son comportement.

La fonction tester_couverture_complete prend en paramètres les nœuds, 
les arêtes du graphe, ainsi que les séquences minimales générées par la méthode UIO. 
Elle parcourt les séquences minimales et construit les chemins correspondants. 
Ensuite, elle vérifie si tous les chemins du graphe sont couverts 
en comparant l'ensemble des chemins couverts avec l'ensemble de tous les chemins possibles.

Le résultat de la couverture complète des chemins (couverture_complete) 
est un booléen qui indique si tous les chemins du graphe sont couverts ou non. 
L'ensemble des chemins couverts (chemins_couverts) est également affiché pour vous permettre de visualiser les chemins effectivement couverts.

Après avoir exécuté la fonction tester_couverture_complete, 
vous pouvez interpréter les résultats de la manière suivante :

Si couverture_complete est True, 
cela signifie que toutes les combinaisons de chemins possibles dans votre graphe sont couvertes 
par les séquences minimales. Votre système a donc une couverture complète des chemins.

Si couverture_complete est False, 
cela signifie qu'il existe au moins un chemin dans le graphe qui n'est pas couvert par les séquences minimales. 
Vous devriez alors réexaminer votre système et les séquences générées pour identifier les chemins manquants et les corriger.

