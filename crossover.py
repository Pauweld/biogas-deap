import random

#ind1 = [[5,10.1,10,20.2,20,20.2,25,10.6,40,7,50,5,60,0]]
#ind2 = [[4,5.1,6,18.2,25,18.2,30,12,40,10,50,7,55,0]]

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
                
    return ind1, ind2

#if __name__ == "__main__":
    #print(crossover(ind1,ind2))
