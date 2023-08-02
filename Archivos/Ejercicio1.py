'''
Generar un archivo que guarde los datospersonales
Crear una funvion que cuente los caracteres ingresados
Crear una funcion que cuente las lineas 

'''
with open("info.txt","w") as archivo:
    archivo.write('Mi nombre es Cesar Luis Fajardo Jimenez\n')
    archivo.write('Mi edad es de 17\n')
    archivo.write('Mi telefono es 3222208389\n')
    archivo.write('Mi correo es fajardo07cesar@gmail.com')

def caracteres_lineas():
    character_counter= line_counter = 0
    stream=open('info.txt','rt')
    lines=stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
        line=stream.readlines(10)
    stream.close()
    print(f"\nEl archivo tiene {character_counter} caracteres")
    print(f"\nEl archivo tiene {line_counter} lineas")
                
        

    

caracteres_lineas()




















