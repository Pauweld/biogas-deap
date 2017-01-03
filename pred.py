import random
import argparse
import pprint

from data_manager import *
from plot import show_plot
from deap import creator
from deap import tools
from deap import base
from evaluate import evaluate

def main(a,b,gen):
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
    #algorithm
    for courbe in range(len(data)-1)
        
        #individus
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        #individual size
        IND_SIZE = 7
        toolbox = base.Toolbox()
        toolbox.register("attr_float", random.random)
        toolbox.register("individual", tools.initCycle, creator.Individual,
                         list(list((toolbox.attr_float,toolbox.attr_float))), IND_SIZE)

        #population
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)
        population = toolbox.population(n=5)
        for p in population:
            print(p)
           show_plot(p)

def fitness(individual,f,num_intrant):
    data = fill_data(f)
    
    return

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
