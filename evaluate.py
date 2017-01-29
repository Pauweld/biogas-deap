import random

from data_manager import *
from plot import *

#individual = [[0,60,1,60,4,60]]

#pour prendre en compte les autres intrants il faut ajouter un argument : tableau des autres individus.
#avec 1 individu par intrant.
def Fitness(individual,f,num_intrant):
    etendue = individual[0][-2]-individual[0][0]
    #MO = matiere organique
    MO = 0.32
    journals = fill_data(f)
    val_random = random.randint(61,121)
    calculee = 0
    reelle = journals[num_intrant-1][val_random]
    
    #(i,k) dans (95-4,0),(96-4,1),...,(96,4)
    #+1 car on ne prend pas le premier jour (jour 0) mais le jour 1
    #range(1 car on veut s'arreter un cran en avance(jour 59)
    for i,k in zip(range(val_random-etendue+1,val_random),range(1,etendue)):
        # 0,1,..,4-k
        #print('jour utilisé ',journals[0][i],'KG',journals[num_intrant][i])
        for j in range(1,etendue-k+1):
            calculee += getValue(individual,j) * float(journals[num_intrant][i]) * MO / 1000
    #print('Calculee',calculee,'Reelle',reelle,'Jour',val_random)
    return abs(float(reelle)-calculee),calculee/abs(float(reelle))

#if __name__ == '__main__':
#Fitness(individual,'donnees.csv',2)
