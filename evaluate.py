import random

def Fitness(individual,f,num_intrant):
    data = fill_data(f)
    r = random.randint(1,58)
    c = float(getValue(individual,r))
    d = float(data[num_intrant][r])
    #print('différence :',float(c)-float(d))
    #print('Taux :',(float(c)-float(d))/float(d))
    return float(c)-float(d),(float(c)-float(d))/float(d)
