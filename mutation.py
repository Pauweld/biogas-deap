import random

def mutation(individual):
    i = random.randint(0,len(individual[0])-1)
    while(i % 2 != 0):
        i = random.randint(0,len(individual[0])-1)
    if(i == 0):
        individual[0][0] = random.randint(0,individual[0][2])
        individual[0][1] = random.uniform(0.0,individual[0][3])
        individual[0][1] = round(individual[0][1], 2)
    elif(i == 12):
        individual[0][12] = random.randint(individual[0][10],60.0)
    else:
        individual[0][i] = random.randint(individual[0][i-2],individual[0][i+2])
        individual[0][i+1] = random.uniform(individual[0][i-1],individual[0][i+3])
        individual[0][i+1] = round(individual[0][i+1], 2)

    return individual
