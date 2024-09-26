import funciones.punto_1, funciones.punto_2, funciones.punto_11

# 1- a
ingresos = funciones.punto_1.ingresos
promedio_20 = funciones.punto_1.calcular_promedio_ingresos(ingresos)
print(f'promedio del 20% que más gana: {promedio_20}')

# b
promedio_todos = funciones.punto_1.calcular_promedio_total(ingresos)
print(f'ingresos totales: {promedio_todos}')

# c
repetidos = funciones.punto_1.calcular_valores_repetidos(ingresos)
print(f'valores que mas se repiten: {repetidos}')

# d
media_geometrica = funciones.punto_1.calcular_media_geometrica(ingresos)
print(f'media geométrica: {media_geometrica}')

# e
adelante, atras = funciones.punto_1.recorrer_lista_ambos_lados(ingresos)
print(f'recorrido para adelante: {adelante}')
print(f'recorrido para atras: {atras}')

# 2- a
lista_edad = funciones.punto_2.lista_edad
lista_nombres = funciones.punto_2.lista_nombres

nombre_joven, edad_mini, nombre_mayor, edad_maxi, media_mayores_40 = funciones.punto_2.devolver_menor_y_mayor(lista_edad, lista_nombres)

print(f'el más joven: {nombre_joven} ({edad_mini} años)')
print(f'el más mayor: {nombre_mayor} ({edad_maxi} años)')
print(f'media de edades mayores de 40: {media_mayores_40}')




