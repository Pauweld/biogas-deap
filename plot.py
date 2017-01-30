# ce fichier permet de gérer les graphes des individus
#(récupérer les abscisses, les ordonnées, enregistrer le graphe et pouvoir lire une ordonnée en fonction d'un abscisse passé en paramètre)

import matplotlib.pyplot as plt
import numpy as np

def getX(ind):
    list = [0]
    for i in range(0,len(ind)):
        if (i%2 == 0):
            list.append(ind[i])
    return list

def getY(ind):
    list = [0]
    for i in range(0,len(ind)):
        if (i%2 == 1):
            list.append(ind[i])
    return list

def show_plot(ind,name):
    listX = getX(ind[0])
    listY = getY(ind[0])
    plt.plot(listX, listY)
    plt.axis([0, max(listX)+2, 0, max(listY)+(0.2*max(listY))])
    plt.xlabel('Temps (jours)')
    plt.ylabel('Quantité de méthane (Nm^3)')
    plt.savefig(str(name)+'.png', bbox_inches='tight')
    plt.clf()
    #plt.show()

def getValue(ind, x):
    listX = getX(ind[0])
    listY = getY(ind[0])
    i = 0
    while x > listX[i]:
        i = i+1
    m,b = np.polyfit([listX[i-1],listX[i]], [listY[i-1],listY[i]], 1)
    return m*x+b
