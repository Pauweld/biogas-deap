# ce fichier implémente la mutation pour un individu donné

import random

ind = [[5,10.1,10,20.2,15,20.2,19,10.6,20,7,30,5,35,0]]

def mutation(individual):
    i = random.randint(0,len(individual[0])-1)
    while(i % 2 != 0):
        i = random.randint(0,len(individual[0])-1)
    if(i == 0):
        individual[0][0] = random.randint(1,individual[0][2])
        individual[0][1] = random.uniform(0.0,individual[0][3])
        individual[0][1] = round(individual[0][1], 2)
    elif(i == 12):
        individual[0][12] = random.randint(individual[0][10],35)
        individual[0][12] = round(individual[0][12], 2)
    elif(i == 2):
        individual[0][2] = random.randint(individual[0][0],individual[0][4])
        individual[0][3] = random.uniform(individual[0][1],individual[0][3])
        individual[0][3] = round(individual[0][3], 2)
        individual[0][5] = individual[0][3]
    elif(i == 4):
        individual[0][4] = random.randint(individual[0][2],individual[0][4])
        individual[0][5] = random.uniform(individual[0][3],individual[0][5])
        individual[0][5] = round(individual[0][5], 2)
        individual[0][3] = individual[0][5]
    else:
        individual[0][i] = random.randint(individual[0][i-2],individual[0][i+2])
        individual[0][i+1] = random.uniform(individual[0][i-1],individual[0][i+3])
        individual[0][i+1] = round(individual[0][i+1], 2)

    return individual

if __name__ == "__main__":

    print(mutation(ind))
