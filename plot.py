import matplotlib.pyplot as plt
import numpy as np

ind = [[5,10.1,10,20.2,20,20.5,25,10.6,40,7,50,5,60,0]]

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
    plt.axis([0, listX[7]+2, 0, listY[2]+2])
    plt.xlabel('Temps (jours)')
    plt.ylabel('Quantité de méthane (m^3)')
    plt.savefig(str(name)+'.png', bbox_inches='tight')
    #plt.show()

def getValue(ind, x):
    listX = getX(ind[0])
    listY = getY(ind[0])
    i = 0
    while x > listX[i]:
        i = i+1
    m,b = np.polyfit([listX[i-1],listX[i]], [listY[i-1],listY[i]], 1)
    return m*x+b
    
#print(getValue(ind, 19))
#show_plot(ind,1)
