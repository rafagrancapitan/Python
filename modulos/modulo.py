"""
Programa:       Número perfecto
Descripción:    Indica si un número es perfecto
                Un número entero positivo es perfecto si
                es igual a la suma de sus divisores

"""

def es_perfecto(numero): 
    suma_divisores = 1
    divisor = 2
    while divisor < numero / 2:
        if numero % divisor == 0:
            suma_divisores += divisor
        divisor = divisor + 1

    # Fin del bucle while
    
    numero_perfecto = suma_divisores == numero
    return numero_perfecto

# Fin de la función es_perfecto


def es_negativo(n) -> bool:
    # Añado comentario y lo modifico
    return True if n < 0 else False

def es_positivo(n) -> bool:
    return True if n > 0 else False


