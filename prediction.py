from data_manager import *
from plot import *


def findColIndex(tab,name):
    for i in range(len(tab)):
        if tab[i][0]==name:
            return int(i)

def prediction(donnees, cinetiques, cinetiques_theo, MO, depart, arrivee):
    #donnees = fill_data(donnees)
    intrants = MO.keys()

    fichier = open('prediction.csv','a')
    fichier.write('Jour;Prod Calculée;Prod Reelle\n')
    for jour in range(depart,arrivee+1):
        #print('Jour: ',donnees[0][jour])
        production_calculee = 0
        for i in intrants:
            for antecedents,j in zip(range(jour-59, jour),range(59,0,-1)):
                #print('Cinetique: ',i,'jour: ',j,'valeur: ',getValue(cinetiques[i],j)) OK
                #print('Intrant:',i,'vrai jour:',donnees[0][antecedents],'valeur:',donnees[findColIndex(donnees,i)][antecedents].replace('\n',''),'Jour intrant: ',j)
                production_calculee += float(getValue(cinetiques[i],j)) * float(donnees[findColIndex(donnees,i)][antecedents].replace('\n','')) * float(MO[i]) / 1000 / 100
                
        #print('production calculee: ',production_calculee, 'production reelle: ',donnees[1][jour])
        fichier.write(str(donnees[0][jour])+';'+str(production_calculee)+';'+str(donnees[1][jour])+'\n')
    fichier.close()

if __name__=='__main__':

    MO = {'Graisse de Flottation': 4,
          'Fumier Bovin': 24,
          'Lisier Porc': 6.3,
          'Ensilage de Mais': 27.13,
          'Mat. Stercoaire': 23.5,
          'Ensilage de CIVE': 31.2
          }

    cinetiques_calculees = {
        'Graisse de Flottation':[[1,7,5,7]],
        'Fumier Bovin':[[1,5,5,5]],
        'Lisier Porc':[[1,9,5,9]],
        'Ensilage de Mais':[[1,15,5,15]],
        'Mat. Stercoaire':[[1,6,5,6]],
        'Ensilage de CIVE':[[1,10,5,10]]
        }

    cinetiques = 'cinetiquesOK.csv'

    donnees = 'donnees.csv'

    #calcul
    prediction(donnees, cinetiques_calculees, cinetiques ,MO, 10, 15)



