from pais import *
import csv
listaPaises=[]
with open('pais.csv') as csvDataFile:
          #C:\Users\SENA\Download\paises.csv

    csvReader=csv.reader(csvDataFile)
    for row in csvReader:
        ob=pais(row[1], row[3], row[7], row[8])
        listaPaises.append(ob)

for paises in listaPaises:
    print('Nombre pais:', paises.getNombre())
    print('Poblacion:', paises.getPoblacion())
    print('Altura:', paises.getAltura())
    print('pop_cap:', paises.getPop_cap())

