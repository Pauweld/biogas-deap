import random
import argparse
import pprint
import numpy

from data_manager import *
from plot import *
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
    ###########
    #deap     #
    ###########

    #individuals
    creator.create("FitnessMin", Fitness, weights=(1,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    #functions
    toolbox = base.Toolbox()
    toolbox.register("attr_item", createIndividual)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                    toolbox.attr_item, 1)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluateInd)

    #population
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    population = toolbox.population(n=5)

    ###########
    #algorithm#
    ###########
    for g in 1:
        #new generation (size(offsprint) < size(population))
        offspring = toolbox.select(population, len(population))
        #clone theses to avoid modifying in the population
        offspring = map(toolbox.clone, offspring)
        #crossover
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            #0.5 = probability to crossever
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        #mutation
        for mutant in offspring:
            if random.random() < 0.02:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        #reevaluate invalid individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        #replacing in the pop
        pop.append(offspring)

    
        
def createIndividual():
    x1 = random.randint(0, 30)
    y1 = random.uniform(0, 500)
    
    x2 = random.randint(x1, 40)
    y2 = 2*y1

    x3 = random.randint(x2, 60)
    y3 = y2

    x4 = random.randint(x3, 60)
    y4 = y1

    x5 = random.randint(x4, 60)
    y5 = random.uniform(0, y4-1)

    x6 = random.randint(x5, 60)
    y6 = random.uniform(0, y5)

    x7 = random.randint(x6, 60)
    y7 = 0
    return [x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7]

def respectConstraints(ind):
    #y2
    if ind[3]:

def Fitness(individual,f,num_intrant):
    data = fill_data(f)
    r = random.randint(0,60)
    c = getValue(individual,r)
    d = data[num_intrant][r]
    print('jour random : ',r)
    print('cinetiques : ',c)
    print('data journalieres : ',d)
    print('différence :',float(c)-float(d))
    print('Taux :',(float(c)-float(d))/float(d))
    return float(c)-float(d),(float(c)-float(d))/float(d)

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
