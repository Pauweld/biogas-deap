import matplotlib.pyplot as plt

ind = [(5,10),(10,20),(20,20),(25,10),(40,7),(50,5),(60,0)]

def getX(ind):
    list = [0]
    for i in range(0,len(ind)):
        list.append(ind[i][0])
    return list

def getY(ind):
    list = [0]
    for i in range(0,len(ind)):
        list.append(ind[i][1])
    return list

def show_plot(ind):
    listX = getX(ind)
    listY = getY(ind)
    plt.plot(listX, listY)
    plt.axis([0, listX[7]+2, 0, listY[2]+2])
    plt.xlabel('Temps (jours)')
    plt.ylabel('Quantité de méthane (m^3)')
    #plt.savefig('plot.png', bbox_inches='tight')
    plt.show()

#show_plot(ind)

