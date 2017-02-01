def fill_data(f):
    fa = open(f,'r')
    data=list()
    ligne = fa.readline()
    taille = len(ligne.split(';'))
    for a in range(taille):
        data.append([])
    while ligne != '':
        ligne = ligne.split(';')
        for c in range(taille):
            data[c].append(ligne[c].replace('\n',''))
        ligne = fa.readline()
    fa.close()
    return data

def chargerCinetiques(f):
    data = fill_data(f)
    #on inverse
    data = list(map(list, zip(*data)))
    intrants = dict()
    MO = dict()
    
    #chargement des MO
    for i in range(1,len(data[0])):
        MO[data[1][i].replace('\n','')] = data[0][i].replace('\n','')

    #chargement des cinetiques
    data = data[1:]
    data = list(map(list, zip(*data)))
    for i in range(1,len(data)):
        intrants[data[i][0].replace('\n','')] = [[]]
        for j in range(1,len(data[i])):
            #print('val',data[i][j])
            valeur = data[i][j].replace('\n','').replace(',','.')
            if valeur != '':
                intrants[data[i][0].replace('\n','')][0].append(j)
                intrants[data[i][0].replace('\n','')][0].append(float(valeur))
    #print(MO)
    #print('\n')
    #print(intrants)
    return MO, intrants
        

if __name__=="__main__":
    #data = fill_data('donnees.csv')
    chargerCinetiques('cinetiquesOK.csv')
    #the production of 'ensillage de CIVE' for the 6th day :
