# ici, on retrouve la structure de l'algo princpial qui sera appelé dans pred.py

import random
import numpy
import os, sys

from plot import *
from deap import creator
from deap import tools
from deap import base
from crossover import *
from evaluate import *
from mutation import *

POP = 100

def GA(a,b,gen,intrant,nom_intrant,MO,CINETIQUES):

    if not os.path.exists('./'+nom_intrant.replace("\n", "")):
        os.mkdir('./'+nom_intrant.replace("\n", ""))
    
    ###########
    #deap     #
    ###########

    #individuals
    creator.create("FitnessMin", base.Fitness, weights=(-1,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    #functions
    toolbox = base.Toolbox()
    toolbox.register("attr_item", createIndividual)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                                    toolbox.attr_item, 1)
    toolbox.register("mate", crossover)
    toolbox.register("mutate", mutation)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", Fitness,f=a,num_intrant=intrant
                     ,M=MO,CINETIQUES=CINETIQUES,nom_intrant=nom_intrant)

    #population
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    population = toolbox.population(n=POP)

    ###########
    #algorithm#
    ###########
    for g in range(gen):
        #new generation (size(offsprint) < size(population))
        # selection de la moitié de la population totale
        offspring = toolbox.select(population, len(population))
        #clone theses to avoid modifying in the population
        offspring = list(map(toolbox.clone, offspring))
        #crossover
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            #0.5 = probability to crossover
            if random.random() < 0.5:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        #mutation
        for mutant in offspring:
            if random.random() < 0.02:
                toolbox.mutate(mutant)
                print('MUTATION : gen'+str(g+1)+'-ind'+str(mutant))
                del mutant.fitness.values
        #reevaluate invalid individuals
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        #replacing in the pop
        population[:] = offspring
        for i in range(len(population)):
            show_plot(population[i],'./'+nom_intrant.replace("\n", "")+'/'+'gen'+str(g+1)+'-ind'+str(i+1)+'-'+nom_intrant.replace("\n", ""))
            #print(population[i].fitness.values)
    return population[0]


# permet de créer de façon aléatoire les individus
def createIndividual():

    x1 = random.randint(1, 3)
    y1 = random.uniform(0, 50)
    
    x2 = random.randint(x1, 8)
    y2 = 2*y1

    x3 = random.randint(x2, 13)
    y3 = y2

    x4 = random.randint(x3, 20)
    y4 = y1

    x5 = random.randint(x4, 25)
    y5 = random.uniform(0, y4-1)

    x6 = random.randint(x5, 30)
    y6 = random.uniform(0, y5)

    x7 = random.randint(x6, 35)
    y7 = 0
    return [x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7]
