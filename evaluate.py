import random

from data_manager import *
from plot import *

individual = [[5,10.1,10,20.2,20,20.5,25,10.6,40,7,50,5,60,0]]

def Fitness(individual,f,num_intrant):
    data = fill_data(f)
    r = random.randint(61,121)
    reelle = data[num_intrant-1][r]
    somme = 0
    for i in range(r-59,r):
        for j in range(i,individual[0][-2]):
            somme += getValue(individual,j) * int(data[num_intrant][i]) / 1000 * 0.32 / 100
    return  abs(float(relle)-somme),somme/float(reelle)
