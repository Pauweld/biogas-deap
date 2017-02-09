# fonction de croisement entre 2 individus

import random
from plot import *

ind1 = [[5,10.1,10,20.2,20,20.2,25,10.6,40,7,50,5,60,0]]
ind2 = [[4,5.1,6,40,10,40,11,35,12,20,13,15,14,0]]

def crossover(ind1, ind2):
    size = len(ind1[0])
    cxpoint = random.randint(1, size - 1)
    while((cxpoint % 2) != 0 or cxpoint == 2 or cxpoint == 4):
        cxpoint = random.randint(1, size - 1)
    ind1[0][cxpoint:], ind2[0][cxpoint:] = ind2[0][cxpoint:], ind1[0][cxpoint:]
    for i in range(cxpoint,len(ind1[0])):
        if(i%2 == 0):
            if(ind1[0][i-2] > ind1[0][i]):
                ind1[0][i] = ind1[0][i-2]
    for i in range(cxpoint,len(ind2[0])):
        if(i%2 == 0):
            if(ind2[0][i-2] > ind2[0][i]):
                ind2[0][i] = ind2[0][i-2]

    if (ind1[0][7] > ind1[0][5]):
        ind1[0][7] = random.uniform(0, ind1[0][5])
        ind1[0][7] = round(ind1[0][7], 2)
    if (ind1[0][9] > ind1[0][7]):
        ind1[0][9] = random.uniform(0, ind1[0][7])
        ind1[0][9] = round(ind1[0][9], 2)
    if (ind1[0][11] > ind1[0][9]):
        ind1[0][11] = random.uniform(0, ind1[0][9])
        ind1[0][11] = round(ind1[0][11], 2)
    if (ind1[0][13] > ind1[0][11]):
        ind1[0][13] = 0

    if (ind2[0][7] > ind2[0][5]):
        ind2[0][7] = random.uniform(0, ind2[0][5])
        ind2[0][7] = round(ind2[0][7], 2)
    if (ind2[0][9] > ind2[0][7]):
        ind2[0][9] = random.uniform(0, ind2[0][7])
        ind2[0][9] = round(ind2[0][9], 2)
    if (ind2[0][11] > ind2[0][9]):
        ind2[0][11] = random.uniform(0, ind2[0][9])
        ind2[0][11] = round(ind2[0][11], 2)
    if (ind2[0][13] > ind2[0][11]):
        ind2[0][13] = 0
                
    return ind1, ind2

if __name__ == "__main__":
    i1, i2 = crossover(ind1,ind2)
    show_plot(i1, 'i1')
    show_plot(i2, 'i2')
