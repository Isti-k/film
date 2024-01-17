from Film import Film

def faljbeolvasas():
    fajl=open("film.txt","r",encoding="UTF-8")
    fajl.readline()
    fajl_sorok=fajl.readlines()
    print(fajl_sorok)
    fajl.close()

    Film_lista=[]
    for i in range(0,len(fajl_sorok),1):
        elem=fajl_sorok[i]#Hős;Yimou Zhang;Jet Li;2002;96
        lista=elem.strip().split(";")#Hős Yimou Zhang Jet Li;2002;96
        print(lista)
        cim:str=str(lista[0])
        rendezo:str=str(lista[1])
        foszereplo:str=str(lista[2])
        ev:int=int(lista[3])
        perc:int=int(lista[4])
        film=Film(cim,rendezo,foszereplo,ev,perc)
        Film_lista.append(film)

    return Film_lista

def legrovidebb_film(Film_lista):
    legrovidebb:int=0
    for i in range(0,len(Film_lista),1):
        if Film_lista[i].perc <= Film_lista[legrovidebb].perc:
            legrovidebb+=i
    return legrovidebb


        






