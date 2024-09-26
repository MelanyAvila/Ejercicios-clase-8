# 1 - Dada la siguiente lista de ingresos horarios:
ingresos = [10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18]

# a) Calcular el promedio de ingresos/hora del 20% que más gana. No es necesario ordenar, se puede usar continue 
# y resolver mediante programación estructurada usando listas.
def calcular_promedio_ingresos(ingresos: list):
    total_ingresos = len(ingresos)
    porcentaje = int(total_ingresos * 0.20)  
    mas_altos = []

    suma_total = 0

    for ingreso in ingresos:
        if len(mas_altos) < porcentaje or ingreso > min(mas_altos):
            if len(mas_altos) == porcentaje:
                mas_altos.remove(min(mas_altos))
            mas_altos.append(ingreso)

    for ingreso in mas_altos:
        suma_total += ingreso

    promedio = suma_total / len(mas_altos)
    return promedio

# b) Calcular el promedio de ingresos/hora de todos los respondentes.
def calcular_promedio_total(ingresos: list):
    suma = 0 
    cantidad = 0  

    for ingreso in ingresos:
        suma += ingreso
        cantidad += 1

    promedio = suma / cantidad
    return promedio

# c) Buscar cuál es el valor que más se repite. En caso de ser varios, devolverlos todos.
def calcular_valores_repetidos(ingresos: list):
    valores_unicos = []  
    repeticiones = []  

    max_repeticiones = 0

    valores_repetidos = []
    
    for ingreso in ingresos:

        encontrado = False

        for i in range(len(valores_unicos)):
            if valores_unicos[i] == ingreso:
                repeticiones[i] += 1  
                encontrado = True
                break

        if not encontrado:
            valores_unicos = valores_unicos + [ingreso]
            repeticiones = repeticiones + [1]

    for repes in repeticiones:
        if repes > max_repeticiones:
            max_repeticiones = repes

    for i in range(len(repeticiones)):
        if repeticiones[i] == max_repeticiones:
            valores_repetidos = valores_repetidos + [valores_unicos[i]]
    return valores_repetidos

# d) Calcular la media geométrica. La media geométrica es la raíz de los productos.
def calcular_media_geometrica(ingresos: list):
    producto = 1 
    n = 0
   
    for ingreso in ingresos:
        producto *= ingreso
    
    for _ in ingresos: 
        n += 1
    
    media_geometrica = producto ** (1 / n)
    return media_geometrica

# e) Crear una función que permita recorrer las listas en ambos sentidos.
def recorrer_lista_ambos_lados(ingresos: list):
    recorrido_adelante = []  
    recorrido_atras = []     

    # adelante
    for item in ingresos:
        recorrido_adelante = recorrido_adelante + [item] 

    # atras
    for i in range(len(ingresos) - 1, -1, -1):
        recorrido_atras = recorrido_atras + [ingresos[i]]  
    return recorrido_adelante, recorrido_atras  

