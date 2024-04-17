def stampaDizionario(diz):
    for key,value in diz.items():
        print("La chiave è "+key)
        print("Il valore è "+str(value))
    
dizionario={"rossi":18,"bianchi":16,"verdi":6}
#inserire un elemento dentro il dizionario
dizionario["viola"]=14
print(dizionario)
#modificare una copia chiave valore
dizionario["bianchi"]=18
print(dizionario)
#iterare sul dizionario
for key,value in dizionario.items():
    print("La chiave è "+key)
    print("Il valore è "+str(value))
#calcolare il totale delle ore del dizionario


def sommatore(diz):
    somma=0
    for key,value in dizionario.items():
        somma+=value    
        print("La somma è "+str(somma))
        cattedraPiena=0   
#numero degli insegnanti con cattedra piena(18h)
def ore (diz):
        for key,value in dizionario.items():
            if value==18:
                cattedraPiena=cattedraPiena+1
                print("I prof con la cattedra piena sono "+str(cattedraPiena))

def cambiaOre(diz,professore,ore): 
    if professore in diz:
          diz[professore]=ore

          
    print(dizionario)
cambiaOre(dizionario,"rossi",8)
print(dizionario)


