#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor

def obtener_notas_alumno():
    notas = []
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10. Inténtelo nuevamente.")
            except ValueError:
                print("Ingrese un número válido.")

    print("Notas del alumno:")
    for nota in notas:
        print(nota)

    nota_media = sum(notas) / len(notas)
    print(f"Nota media: {nota_media:.2f}")

    nota_maxima = max(notas)
    nota_minima = min(notas)
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")

obtener_notas_alumno()
