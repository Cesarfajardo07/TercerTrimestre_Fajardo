import csv

personas= [
    ['Palacios','Rivas','Adan','CDMX'],
    ['Torres','Palacios','Sandra','MORELIA'],
    ['Martinez','Martinez','Jose','TIJUANA'],
]

with open('personas.csv','w', newline='') as archivo:
    writer=csv.writer(archivo,delimiter=';')
    writer.writerows(personas)
    #writer.writerow(personas)
   
with open('personas.csv','r') as archivo:
    reader = csv.reader(archivo, delimiter=';')
    for row in reader:
        print("Ap paterno: {0}, Ap materno: {1}, Nombre: {2}, Ciudad: {3}".format(row[0], row[1], row[2], row[3]))