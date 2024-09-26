# 2- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
# cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

# a) Devolver el nombre del respondiente más jóven y del más grande.
# b) Usando break, busque en la lista si hay mayores de 65. En ese caso cortar la
# iteración y mostrar mensaje por pantalla.
# c) Utilizando continue, calcule la media etaria para mayores de 40 años

def devolver_menor_y_mayor(lista_edad: list, lista_nombres: list):
    nombres_jovenes = []
    nombres_mayores = []

    edad_minima = lista_edad[0]
    edad_maxima = lista_edad[0]

    suma_mayores_40 = 0

    contador_mayores_40 = 0

    for j in range(len(lista_edad)):
        edad_actual = lista_edad[j]
        nombre_actual = lista_nombres[j]

        # a) b) 
        if edad_actual < edad_minima:
            nombres_jovenes = [nombre_actual]
            edad_minima = edad_actual
        elif edad_actual == edad_minima:
            nombres_jovenes.append(nombre_actual)

        if edad_actual > edad_maxima:
            nombres_mayores = [nombre_actual]
            edad_maxima = edad_actual
        elif edad_actual == edad_maxima:
            nombres_mayores.append(nombre_actual)

        # c) 
        if edad_actual < 40:
            continue 
        suma_mayores_40 += edad_actual
        contador_mayores_40 += 1
        if contador_mayores_40 > 0:
            media_mayores_40 = suma_mayores_40 / contador_mayores_40
        else:
            media_mayores_40 = 'no hay personas mayores de 40'
    return nombres_jovenes, edad_minima, nombres_mayores, edad_maxima, media_mayores_40

 
