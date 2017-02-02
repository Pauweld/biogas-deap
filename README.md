# biogas-deap : This is a projet featured with Biosgas View company. The purpose is to make prediction of methane production with Genetic Algorithms

To run the algorithm you need to have 2 files : one which contains the daily production and intrants, the second which contains the cinetics. The two
files have to contain the same intrants.

To run : python main.py -d %1 -c %2 -g %3 -t %4
With %1 the name of the daily file, %2 the name of the cintetics file, %3 the number of the generations and %4 the number of rounds.

example : python main.py -d donnees.csv -c cinetiques.csv -g 10 -t 1