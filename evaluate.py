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
    num_intrant = findColIndex(journals,nom_intrant)
    val_random = random.randint(61,121)
    #val_random = 8
    calculee = 0
    reelle = journals[1][val_random]

    #print('jour a calculer',journals[0][val_random])
    
    #(i,k) dans (95-4,0),(96-4,1),...,(96,4)
    #+1 car on ne prend pas le premier jour (jour 0) mais le jour 1
    #range(1 car on veut s'arreter un cran en avance(jour 59)
    for i,k in zip(range(val_random-etendue+1,val_random),range(1,etendue)):
        # 0,1,..,4-k
        #print('AUTRE JOUR ********************')
        for j in range(1,etendue-k+1):
            #print('jour utilisé ',journals[0][i],'intrant utilisé:',(journals[num_intrant][0]),'KG:',journals[num_intrant][i])
            calculee += getValue(individual,j) * float(journals[num_intrant][i]) * MO / 1000
            #print(journals[0][i],'jour',j,'calcul:',getValue(individual,j),'*',float(journals[num_intrant][i]),'*',MO,'/',1000,'=',getValue(individual,j) * float(journals[num_intrant][i]) * MO / 1000)
            it = iter(C_temp)
            for cle in it:
                M_temp = float(M[cle].replace(',','.'))
                calculee += getValue(C_temp[cle],j)*(float(journals[findColIndex(journals,cle)][i])/1000)*M_temp
                #print(getValue(C_temp[cle],j)*(float(journals[findColIndex(journals,cle)][i])/1000)*M_temp)
                #print(cle,'jour:',j,'valeur:',journals[findColIndex(journals,cle)][i],'MO:',M_temp,'calcul : ',getValue(C_temp[cle],j) ,'*',float(journals[findColIndex(journals,cle)][i]),'*',M_temp,'/1000 = ',getValue(C_temp[cle],j)*float(journals[findColIndex(journals,cle)][i])/1000*M_temp)
    #print('calculee',calculee)
    print("reelle-calculee : ",abs(float(reelle)-calculee))
    return abs(float(reelle)-calculee), 1/7

def findColIndex(tab,name):
    for i in range(len(tab)):
        if tab[i][0]==name:
            return int(i) 

if __name__ == '__main__':
    #print(findColIndex('','Lisier Porc'))

    individual = [[1,5,5,5]]
    f = 'donnees.csv'
    num_intrant = 1
    M = {'Graisse de Flottation': '4', 'Fumier Bovin': '24', 'Lisier Porc': '6,3', 'Ensilage de Mais': '27,13', 'Mat. Stercoaire': '23,5', 'Ensilage de CIVE': '31,2'}
    CINETIQUES = {'Graisse de Flottation':[[1,7,5,7]],
                  'Fumier Bovin': [[1,5,5,5]],
                  'Lisier Porc': [[1,9,5,9]],
                  'Ensilage de Mais': [[1,15,5,15]],
                  'Mat. Stercoaire': [[1,6,5,6]],
                  'Ensilage de CIVE': [[1,10,5,10]]}

    Fitness(individual,f,num_intrant,M,CINETIQUES,'Fumier Bovin')



