# biogas-deap : Projet en collaboration avec Biogas View

Pour exectuer le programme vous avez besoin des m�mes intrants dans les 2 fichiers (cin�tiques et journali�res).

INSTALLATION (Windows):

$ python -m pip install numpy

$ python -m pip install matplotlib

$ python -m pip install deap

EXECUTION: 

python main.py -d %1 -c %2 -g %3 -t %4
Avec %1 le nom du fichier des donn�es journali�res, %2 le nom du fichiers des donn�es cin�tiques, %3 le nombre de g�n�rations et %4 le nombre de tours.

Exemple : python main.py -d donnees.csv -c cinetiquesOK.csv -g 10 -t 1


