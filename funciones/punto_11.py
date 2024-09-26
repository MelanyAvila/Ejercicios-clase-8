# 11- Programar el algoritmo de búsqueda binaria de forma recursiva
lista_ejemplo = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
valor_buscado = 18

inicio = 0
final = len(lista_ejemplo) - 1

def buscar_binario_recursivo(lista: list, buscado: any, inicio: int, final: int):    
    if inicio > final: 
        return None
    medio = (inicio + final) // 2
    
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return buscar_binario_recursivo(lista, buscado, medio + 1, final) 
    else:
        return buscar_binario_recursivo(lista, buscado, inicio, medio - 1)

resultado = buscar_binario_recursivo(lista_ejemplo, valor_buscado, inicio, final)

if resultado is None:
    print(f'valor {valor_buscado} no encontrado')
else:
    print(f'valor {valor_buscado} encontrado en el índice: {resultado}')
    
