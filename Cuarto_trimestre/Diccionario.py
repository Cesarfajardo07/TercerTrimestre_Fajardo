def agregar_alumnos():
    alumnos = {}
    num_alumnos = int(input("Ingrese el número de alumnos: "))

    for _ in range(num_alumnos):
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        if nombre_alumno in alumnos:
            print(f"¡Error! El alumno '{nombre_alumno}' ya existe en la lista.")
            continue

        notas_alumno = []
        nota = float(input(f"Ingrese la nota del alumno '{nombre_alumno}' (ingrese un número negativo para finalizar): "))
        
        while nota >= 0:
            notas_alumno.append(nota)
            nota = float(input("Ingrese otra nota (ingrese un número negativo para finalizar): "))
        
        alumnos[nombre_alumno] = notas_alumno

    print("\nNotas de los alumnos y su nota media:")
    for nombre, notas in alumnos.items():
        nota_media = sum(notas) / len(notas)
        print(f"{nombre}: {notas} - Nota media: {nota_media:.2f}")

agregar_alumnos()
