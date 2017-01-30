# ceci est le main
# il appelle tous les autres .py

import random
import argparse
import pprint
import numpy
import time

from GA import *
from data_manager import *
from plot import *
from deap import creator
from deap import tools
from deap import base
from crossover import *
from evaluate import *
from mutation import *

def main(a,b,gen):
    print('-----------------DEBUT-----------------')
    tps1 = time.clock()
    #data
    fa = open(a,'r')
    header = fa.readline()
    nb_intrants_d = len(header.split(';'))-2
    name_intrants_d = header.split(';')[2:]
    fa.close()
    
    #cinetics
    fb = open(b,'r')
    header = fb.readline()
    nb_intrants_c = len(header.split(';'))-1
    name_intrants_c = header.split(';')[1:]
    fb.close()

    #check compatibility
    if nb_intrants_c != nb_intrants_d:
        print('Fichiers érronés')
        return
    for i in name_intrants_c:
        if i not in name_intrants_d:
            print('Fichiers érronés')
            return
    data = fill_data(a)
    cinetiques = fill_data(b)

    #list which would contain each curve of each intrant
    null_individual = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    cinetics_list = dict()
    for i in range(nb_intrants_c):
        cinetics_list[name_intrants_c[i]] = null_individual
        
    #########
    for i in name_intrants_c:
        #we find the indice of the intrant
        for j in range(len(cinetiques)):
            if cinetiques[j][0] == i:
                intrant = j
        #we launch the GA for this intrant
        print('--------------------GA for',i.replace("\n", ""),'--------------------')
        meilleur_individu = GA(a,b,gen,intrant,i)
    #########
    
    tps2 = time.clock()
    print('-----------------FIN-----------------')
    print('Nombre d\individus :',10)
    print('Temps d\'execution pour',gen,'génération(s) :',tps2 - tps1)


        



if __name__ == "__main__":
    #arguments
    parser = argparse.ArgumentParser(
    description="Get stats from Powertool output")
    parser.add_argument('-d', '--donnees', type=str, default='donnees.csv',
                        required = True,
                        help="Data in .csv format")
    parser.add_argument('-c', '--cinetiques', type=str, default='cinetiques.csv',
                        required = True,
                        help="Cinetic curves in .csv format")
    parser.add_argument('-g', '--generations', type=int, default=100, required=True,
                        help="Number of generations to make")
    args = parser.parse_args()
    
    #start 
    main(args.donnees,args.cinetiques,args.generations)
