# biogas-deap : Projet en collaboration avec Biogas View

Pour exectuer le programme vous avez besoin des mêmes intrants dans les 2 fichiers (cinétiques et journalières).

INSTALLATION (Windows):

$ python -m pip install numpy

$ python -m pip install matplotlib

$ python -m pip install deap

EXECUTION: 

python main.py -d %1 -c %2 -g %3 -t %4
Avec %1 le nom du fichier des données journalières, %2 le nom du fichiers des données cinétiques, %3 le nombre de générations et %4 le nombre de tours.

Exemple : python main.py -d donnees.csv -c cinetiquesOK.csv -g 10 -t 1


