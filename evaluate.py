import random

individual = [[5,10.1,10,20.2,20,20.5,25,10.6,40,7,50,5,60,0]]

def Fitness(individual,f,num_intrant):
    data = fill_data(f)
    r = random.randint(60,120)
    reelle = data[num_intrant-1][r])
    somme = 0
    for i,j in zip(range(r-60,r),range(1,60)):
        somme += getValue(individual,j) * int(data[num_intrant][i])
    return  somme,somme/reelle
