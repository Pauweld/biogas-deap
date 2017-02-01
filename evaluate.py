# la fonction d'évaluation qui prend en compte les individus générés et les .csv

import random

from data_manager import *
from plot import *

#individual = [[0,60,1,60,4,60]]

#pour prendre en compte les autres intrants il faut ajouter un argument :
#tableau des autres individus avec 1 individu par intrant.

def Fitness(individual,f,num_intrant,M,CINETIQUES,nom_intrant):
    C_temp = dict(CINETIQUES)
    del C_temp[nom_intrant.replace('\n','')]
    #it = iter(C_temp)
    
    etendue = individual[0][-2]-individual[0][0]
    #MO = matiere organique
    MO = float(M[nom_intrant.replace('\n','')].replace(',','.'))
    journals = fill_data(f)
    val_random = random.randint(61,121)
    calculee = 0
    reelle = journals[num_intrant][val_random]

    
    #(i,k) dans (95-4,0),(96-4,1),...,(96,4)
    #+1 car on ne prend pas le premier jour (jour 0) mais le jour 1
    #range(1 car on veut s'arreter un cran en avance(jour 59)
    for i,k in zip(range(val_random-etendue+1,val_random),range(1,etendue)):
        # 0,1,..,4-k
        #print('jour utilisé ',journals[0][i],'KG',journals[num_intrant][i])
        for j in range(1,etendue-k+1):
            calculee += getValue(individual,j) * float(journals[num_intrant+1][i]) * MO / 1000
            it = iter(C_temp)
            for cle in it:
                M_temp = float(M[cle].replace(',','.'))
                #print(cle,'jour:',j,'valeur:',journals[findColIndex(journals,cle)][i],'MO:',M_temp)
                calculee += getValue(C_temp[cle],j) * float(journals[findColIndex(journals,cle)][i]) * M_temp / 1000
    #print('Calculee',calculee,'Reelle',reelle,'Jour',val_random)
    return abs(float(reelle)-calculee),calculee/abs(float(reelle))

def findColIndex(tab,name):
    for i in range(len(tab)):
        if tab[i][0]==name:
            return int(i) 
    

#if __name__ == '__main__':
    #Fitness(individual,'donnees.csv',2)
    #print(findColIndex('','Lisier Porc'))

    
