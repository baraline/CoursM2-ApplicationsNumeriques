## Sujet : Créer un algorithme de transformation par shapelet

Le but de ce TP est de créer un algorithme de transformation par shapelet. Une base de code vous est fourni dans le fichier `student_method.py` que vous devrez compléter pour créer votre algorithme.

Le code déjà en place vous propose :

- Une structure de classe utilisant les interfaces de scikit-learn (fit/transform) que vous devez conserver.
    
- Des fonctions pour le calcul du vecteur de distance entre des séries et une shapelet. Bien que ces fonctions soient assez rapides, la structure du code peut être optimisée pour éviter de recalculer certain élément et ainsi gagner en performance sur le temps d'exécution.
    
- Votre principale préoccupation sera la partie de génération des shapelets. Vous utiliserez pour cela l'approche de votre choix, parmi celles vu en cours ou une de votre propre invention.
    
    
Pour pimenter un peu cet exercice, je vous propose une petite compétition. Je vous fournis également un fichier `benchmark.py`, qui va vous permettre de tester votre méthode sur différents jeux de données.

- la fonction `run_test_protocol()` lancera votre méthode sur un seul jeu de donnée. C'est cette fonction que vous allez utiliser pour vérifier que tout se passe bien dans l'exécution de votre code. Elle produira un CSV contenant le résultat de votre méthode sur des données de test.
    
- la fonction `run_benchmark_protocol()` lancera votre méthode sur tous les jeux de données sélectionnés pour cette compétition. Elle produira aussi un CSV contenant le résultat de votre méthode sur des données de test ainsi que le résultat moyen sur l'ensemble des jeux de données.
    
- par défaut dans le fichier `benchmark.py`, j'utilise une RandomForest comme classifieur. Vous pouvez si vous le souhaitez modifier le classifieur !
    
Via une console Python, si l'installation du package c'est bien passé, vous devriez pouvoir éxecuter :
```python
from m2tpdm import run_test_protocol
run_test_protocol()
```
    
Si vous souhaitez participer à cette mini compétition, je vous invite à m'envoyer votre code et vos résultats à l'adresse antoine.guillaume@worldline.com, le classement sera affiché sur la page du cours et sera conservé chaque année ! Le classement sera fonction de l'accuracy sur les données de test, mais également sur la vitesse de traitement de votre algorithme.

Il n'y a aucune limite aux modifications que vous pouvez apporter au code, la seule condition est de conserver le fonctionnement fit/transform pour que les script de benchmark fonctionnent.
