# 3- Programar un algoritmo que permita crear una nueva lista de respondentes de manera
# secuencial. Deberán ingresar su nombre, sexo, cantidad de horas trabajadas e ingreso
# semanal en listas separadas.

def recolectar_datos():
    nombres = []
    sexos = []
    horas_trabajadas = []
    ingreso_semanal = []

    for i in range(1, datos + 1):
        nombre = input(f'ingrese el nombre {i}: ')
        sexo = input(f'ingrese el sexo f/m {i}: ')
        horas = int(input(f'ingrese las horas trabajadas {i}: '))
        ingreso = float(input(f'ingrese el ingreso semanal {i}: '))

        nombres.append(nombre)
        sexos.append(sexo)
        horas_trabajadas.append(horas)
        ingreso_semanal.append(ingreso)

    return nombres, sexos, horas_trabajadas, ingreso_semanal

cantidad_respondentes = int(input('ingrese el numero de respondentes: '))
datos = cantidad_respondentes
nombres, sexos, horas, ingresos = recolectar_datos()

print(f'nombres: {nombres}')
print(f'sexos: {sexos}')
print(f'horas trabajadas: {horas}')
print(f'ingresos semanales: {ingresos}')

# 5- Realizar una función que permita corregir las listas del ejercicio 3 en caso de ser
# necesario. Para ello se debe poder acceder a una posición particular y cargar nuevos
# valores para el listado con valor incorrecto en dicha posición.
def corregir_datos(nombres: str, sexos: str, horas_trabajadas: int, ingresos_semanales:float):

    posicion = int(input('ingrese la posición del dato a corregir (empezando desde 1): '))
    posicion -= 1  #para que empiece desde el 0

    nuevo_nombre = input('ingrese el nuevo nombre: ')
    nuevo_sexo = input('ingrese el nuevo sexo f/m: ')
    nuevas_horas = int(input('ingrese las nuevas horas trabajadas: '))
    nuevo_ingreso = float(input('ingrese el nuevo ingreso semanal: '))

    nombres[posicion] = nuevo_nombre
    sexos[posicion] = nuevo_sexo
    horas_trabajadas[posicion] = nuevas_horas
    ingresos_semanales[posicion] = nuevo_ingreso

    print('datos actualizados')
    return nombres, sexos, horas_trabajadas, ingresos_semanales

corregir = input('quiere corregir algún dato? (s/n): ')
if corregir == 's':
    nombres, sexos, horas, ingresos = corregir_datos(nombres, sexos, horas, ingresos)

print(f'nombres: {nombres}')
print(f'sexos: {sexos}')
print(f'horas trabajadas: {horas}')
print(f'ingresos semanales: {ingresos}')