from pais import *
import csv
listaPaises=[]
with open('C:\Users\SENA\Download\paises.csv',) as paiscsv:

    csvReader=csv.reader(paiscsv)
    for row in csvReader:
        ob=pais(row[1], row[2], row[3], row[4])
        listaPaises.append(ob)
        print('')