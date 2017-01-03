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
            data[c].append(ligne[c])
        ligne = fa.readline()
    fa.close()
    return data

if __name__=="__main__":
    data = fill_data('donnees.csv')
    cinetiques = fill_data('cinetiques.csv')
    #the production of 'ensillage de CIVE' for the 6th day :
    print(cinetiques[1][6])
